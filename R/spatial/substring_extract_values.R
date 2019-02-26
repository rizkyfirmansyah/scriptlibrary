library(rgdal)
library(dplyr)

ha <- readOGR("papua_iuphhk_ha_17.shp")
hti <- readOGR("papua_iuphhk_hti_0717.shp")
logging <- readOGR("papua_logging_concessions.shp")


extract_year <- function(text, num_char) {
  text[] <- lapply(text, as.character)
  year <- substr(text, nchar(text) - (num_char - 1), nchar(text))
  
  new_year <- c()
  for(y in c(year)) {
    if (grepl("^[0-1]", y)) {
      new_year <- c(new_year, (paste0("20", y)))
    } else if (grepl("[8?9]", y)) {
      new_year <- c(new_year, (paste0("19", y)))
    } else {
      new_year <- c(new_year, "")
    }
  }
  return(new_year)
}

ha_no_sk <- extract_year(as.character(ha$no_sk), 2)
ha$year <- ha_no_sk

hti_no_sk <- extract_year(as.character(hti$no_sk), 2)
hti$year <- hti_no_sk

logging_year <- extract_year(as.character(logging$permit_num), 2)
logging$year <- logging_year
View(logging)

writeOGR(ha, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Deforestation Papua/Data", "papua_iuphhk_ha_17", "ESRI Shapefile", overwrite_layer = TRUE)
writeOGR(hti, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Deforestation Papua/Data", "papua_iuphhk_hti_0717", "ESRI Shapefile", overwrite_layer = TRUE)
writeOGR(logging, "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Deforestation Papua/Data", "papua_logging_concessions", "ESRI Shapefile", overwrite_layer = TRUE)
View(logging)

#References
#http://www.gastonsanchez.com/r4strings/stringr-basics.html