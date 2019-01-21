library(data.table)

files <- list.files(path = "/", pattern = ".csv")
temp <- lapply(files, fread, sep = ",")
data <- rbindlist(temp)



# writing to xlsx

library(xlsx)
write.xlsx(data, "Drivers of Deforestation TCL 2001 - 2016.xlsx", sheetName = "drivers_all_year", showNA = FALSE)

