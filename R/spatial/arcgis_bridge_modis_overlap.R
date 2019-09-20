library(arcgisbinding)
library(tidyr)
library(stringr)
library(dplyr)
library(rJava)
library(xlsx)

# initialize arcgis binding
arc.check_product()

# Reading arcgis vector data

directory = "D:/DATA/GEOSPATIAL/OPEN_DATA/Burn_Area/burn_area_idn.gdb/"
gis_data <- arc.open(path = file.path(directory, "MCD64_burn_idn_2001_2019_mor"))
out_dir <- "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Norway/Deforestation Hotspot Moratorium"

# Load dataset to R dataframe
r_data <- arc.select(gis_data)

# filter specific column you only need
modis_burn_idn <- r_data %>% select(OBJECTID, burn_day = starts_with("Burn"), burn_year = starts_with("year"), PIPPIB_15, area_ha)
# replace 0 value with NA
modis_burn_idn[modis_burn_idn == 0] <- NA

# Cleaning the column from wide to long format
modis_burn_idn_clean <- unite(modis_burn_idn, burn_day, burn_day1:burn_day19, sep = ",", na.rm = TRUE) %>% mutate(burn_day = str_replace_all(burn_day, 'NA,?', ''))
modis_burn_idn_clean <- unite(modis_burn_idn_clean, burn_year, burn_year1:burn_year19, sep = ",", na.rm = TRUE) %>% mutate(burn_year = str_replace_all(burn_year, 'NA,?', ''))

# Cleaning up the value in moratorium column
modis_burn_idn_clean$PIPPIB_15 <- ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_GAMBUT', 'Moratorium on Peatland',
                                   ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_KAWASAN', 'Moratorium on Watershed Protection Forest',
                                          ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_PRIMER', 'Moratorium on Primary Forest', '')))

modis_burn_2001_2019 <- subset(modis_burn_idn_clean, !is.na(modis_burn_idn_clean$burn_day) | !is.na(modis_burn_idn_clean$burn_year))

# removing the last comma in the string
modis_burn_2001_2019$burn_day <- gsub(",$", "", modis_burn_2001_2019$burn_day)
modis_burn_2001_2019$burn_year <- gsub(",$", "", modis_burn_2001_2019$burn_year)

# grouping and summarise the hectare
modis_burn_2001_2019_cl <- modis_burn_2001_2019 %>% select(burn_year, PIPPIB_15, area_ha) %>% 
  group_by(burn_year, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(moratorium = PIPPIB_15)

modis_burn_2001_2019_cl2 <- subset(modis_burn_2001_2019_cl, modis_burn_2001_2019_cl$burn_year != "") %>%
    mutate(moratorium = replace(moratorium, NA, 'Outside Moratorium'))

# counting the multiple year into new column
modis_burn_2001_2019_cl2$count_year <- lapply(modis_burn_2001_2019_cl2$burn_year, str_count, ",")    

modis_burn_2001_2019_cl2$count_year <- as.numeric(modis_burn_2001_2019_cl2$count_year)
modis_burn_2001_2019_cl2 <- modis_burn_2001_2019_cl2 %>% mutate(count_year = count_year + 1)



# Exporting the data
write.csv(modis_burn_2001_2019_cl2, file.path(out_dir, "modis_burn_area_2001_2019.csv"))
#write.xlsx(modis_burn_2001_2019_cl, file.path(out_dir, "Modis Burn Area 2001 - 2019.xlsx"), sheetName="burn", showNA = FALSE)