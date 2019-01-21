require("RPostgreSQL")

library(readxl)
sample_interpretation <- read_excel("D:/WRI/Research & Analysis/Forest Cover/Sample_interpretation_summary_12122017_ZS.xlsx", sheet="Sample_interpretation_summary")

library(sqldf)

papua <- sqldf("SELECT * FROM sample_interpretation WHERE ID <= 2172")
jawa <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 2172 AND ID <= 2874")
kalimantan <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 2874 AND ID <= 5702")
maluku <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 5702 AND ID <= 6115")
nusa_tenggara <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 6115 AND ID <= 6496")
sulawesi <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 6496 AND ID <= 7483")
sumatera <- sqldf("SELECT * FROM sample_interpretation WHERE ID > 7483 AND ID <= 10000")

# make an aggregation table
library(reshape)
papua_pt <- cast(papua, USER ~ LAND_COVER_1990)
jawa_pt <- cast(jawa, USER ~ LAND_COVER_1990)
kalimantan_pt <- cast(kalimantan, USER ~ LAND_COVER_1990)
maluku_pt <- cast(maluku, USER ~ LAND_COVER_1990)
nusa_tenggara_pt <- cast(nusa_tenggara, USER ~ LAND_COVER_1990)
sulawesi_pt <- cast(sulawesi, USER ~ LAND_COVER_1990)
sumatera_pt <- cast(sumatera, USER ~ LAND_COVER_1990)

# adding column within table
papua_pt$total <- rowSums(papua_pt)
jawa_pt$total <- rowSums(jawa_pt)
kalimantan_pt$total <- rowSums(kalimantan_pt)
maluku_pt$total <- rowSums(maluku_pt)
nusa_tenggara_pt$total <- rowSums(nusa_tenggara_pt)
sulawesi_pt$total <- rowSums(sulawesi_pt)
sumatera_pt$total <- rowSums(sumatera_pt)

# extracting specific column
jawa_pt[c(1), c(2:5)] # c(row, column)

# correlations
cor(jawa_pt[,c(2:5)])

install.packages("Hmisc")
library(Hmisc)


##################### OTHER DATASET #############

forest_legal_forest_loss <- read.csv("C:/Users/rizky/Documents/GEOSPATIAL/ADHOC ANALYSIS/Deforestation/Result/forest_legal_forest_loss.csv", stringsAsFactors = FALSE)

ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`, label = sprintf("%0.2f", round(`Areal Penggunaan Lain`, digits = 2)))) +
    geom_bar(stat = "identity", fill = "deeppink") +
    geom_text(size = 3, vjust = 1.2, fontface = "bold") +
    theme_classic() +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo) +
    geom_smooth(method = "lm", formula = y ~ x, se = FALSE) +
	labs(x = "Year", y = "Non Forest", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))
	

ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`, label = sprintf("%0.2f", round(`Areal Penggunaan Lain`, digits = 2)))) +
    geom_line(stat = "identity", colour = "deeppink") +
    # geom_text(size = 3, vjust = 1.2, fontface = "bold") +
	theme(legend.position = "bottom", legend.background = element_blank(), panel.grid = element_blank(), panel.background = element_blank()) +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo, limits = c(0, 500)) +
	labs(x = "Year", y = "Non Forest (thousands of Ha)", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))	

## line
ggplot() +
    geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Konservasi`, colour = "Conservation Forest")) +
	geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Produksi`, colour = "Production Forest")) +
	geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Lindung`, colour = "Protected Forest")) +
    # geom_text(size = 3, vjust = 1.2, fontface = "bold") +
	theme(legend.position = "bottom", legend.background = element_blank(), panel.grid = element_blank(), panel.background = element_blank()) +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo, limits = c(0, 500)) +
	labs(x = "Year", y = "Forest (thousands of Ha)", colour = "Legend", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))


### SETTING UP A CONN THROUGH POSTGRESQL ###

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "postgres", host = "localhost", port = 5432, user = "postgres", password = "")

## checking the table if exists
dbExistsTable(con, "sample_summary_umd")
## retrieving data and assigning to R data frame
sample_summary_umd = dbGetQuery(con, "select * from sample_summary_umd")

## Close the connection
dbDisconnect(con)
dbUnloadDriver(drv)

# References
# https://rstudio-pubs-static.s3.amazonaws.com/240657_5157ff98e8204c358b2118fa69162e18.html
# http://www.sthda.com/english/wiki/correlation-matrix-a-quick-start-guide-to-analyze-format-and-visualize-a-correlation-matrix-using-r-software