# Importing data from excel

library(readxl)
library(xlsx)
library(sqldf)
library(readr)

forest_2011 <- read_excel("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/Results/Excel Reports/TCL_Forest_LC_11_15.xlsx", sheet = "2011"
    col_types = c("text", "text", "numeric", 
        "skip", "skip", "skip", "skip", 
        "skip"))
View(forest_2011)


# Using sql as your selecting dataframe
dp1 <- sqldf("SELECT No, lower(Provinsi) 'Provinsi', lower([Tutupan Lahan]) as 'Tutupan', [Jumlah Plot] 'jml_plot', d_20, d_50 FROM potensi")
dp2 <- sqldf("SELECT lower([Penutupan Lahan]) as 'Tutupan', lower(Provinsi) 'Provinsi', [Kehilangan tutupan hutan (ha)] as 'loss' FROM TCL_Forest_LC_11_15")

# full outer join all = TRUE
join_tables <- merge(dp1, dp2, all = TRUE)
View(join_tables)

# for export to txt file
write.table(join_tables, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi_tegakan_dan_hilang_tutupan.xlsx", sep="/t")

# for writing to xls file; Needed Java JRE to your PATH env variable
write.xlsx(join_tables, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi_tegakan_dan_hilang_tutupan.xlsx", sheetName="Data Mentah")
## Otherwise using library(openxlsx)
df <- read.xlsx("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi_tegakan_dan_hilang_tutupan.xlsx")
write.xlsx(df, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi_tegakan_dan_hilang_tutupan.xlsx")


#############

potensi <- read_csv("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi.csv")
View(potensi)

forest_loss_2012 <- read_excel("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/Results/Excel Reports/TCL_Forest_LC_11_15.xlsx", 
    sheet = "2012", col_types = c("text", 
        "text", "numeric", "numeric", "skip", 
        "skip", "skip", "skip"))
forest_loss_2012[,1:2] <- apply(forest_loss_2012[,1:2], 2, tolower)

forest_2012 <- read_excel("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/Results/Excel Reports/TCL_Forest_LC_11_15.xlsx", 
    sheet = "2012", col_types = c("skip", 
        "skip", "skip", "skip", "skip", 
        "text", "text", "numeric"))
# lowering all rows within selected column
forest_2012[,1:2] <- apply(forest_2012[,1:2], 2, tolower)

forest_2013 <- read_excel("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/Results/Excel Reports/TCL_Forest_LC_11_15.xlsx", 
    sheet = "2013", col_types = c("skip", 
        "skip", "skip", "skip", "skip", 
        "text", "text", "numeric"))
forest_2013[,1:2] <- apply(forest_2013[,1:2], 2, tolower)
		
forest_loss_2013 <- read_excel("D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/Results/Excel Reports/TCL_Forest_LC_11_15.xlsx", 
    sheet = "2013", col_types = c("text", 
        "text", "numeric", "numeric", "skip", 
        "skip", "skip", "skip"))
		
# removing NA lies in the last rows
forest_loss_2013 <- subset(forest_loss_2013, !is.na(forest_loss_2013[,1]))
forest_loss_2013[,1:2] <- apply(forest_loss_2013[,1:2], 2, tolower)

# Changing the column names
colnames(potensi) <- c("No", "provinsi", "tutupan", "jml_plot", "d_20", "d_50")
colnames(forest_2012) <- c("tutupan", "provinsi", "tutupan_ha")
colnames(forest_loss_2012) <- c("tutupan", "provinsi", "loss_ha", "kosong")
colnames(forest_2013) <- c("tutupan", "provinsi", "tutupan_ha")
colnames(forest_loss_2013) <- c("tutupan", "provinsi", "loss_ha", "kosong")

#
pt_loss_2013 = merge(forest_2013, potensi, all=TRUE)
pt_loss_2013_final = merge(forest_loss_2013, pt_loss_2013, all=TRUE)

#
write.xlsx(pt_loss_2012_final, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/potensi_tegakan_dan_hilang_tutupan.xlsx", sheetName="Canopy Loss 2012", append=TRUE, showNA=FALSE)

recap_2012 <- sqldf("SELECT pulau, r.provinsi, r.tutupan, r.d_20, r.d_50, total, loss_ha 'loss_2012' FROM recap r LEFT JOIN pt_loss_2012_final pl USING(provinsi, tutupan, d_20, d_50)")

write.csv(recap_2015, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Fiscal Transfer/References/recap_2015.csv", na="")
