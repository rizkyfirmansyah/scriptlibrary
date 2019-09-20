library(arcgisbinding)
library(tidyr)
library(stringr)
library(dplyr)
library(rJava)
library(xlsx)

# Reading arcgis vector data

directory = "D:/DATA/GEOSPATIAL/OPEN_DATA/Burn_Area/burn_area_idn.gdb/"
gis_data <- arc.open(path = file.path(directory, "MCD64_burn_idn_2001_2019_mor"))
out_dir <- "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Norway/Deforestation Hotspot Moratorium"

# Load dataset to R dataframe
r_data <- arc.select(gis_data)

modis_burn_idn <- r_data %>% select(OBJECTID, burn_day = starts_with("Burn"), burn_year = starts_with("year"), PIPPIB_15, area_ha)
# replace 0 value with NA
modis_burn_idn[modis_burn_idn == 0] <- NA

'
modis_burn_idn_clean <- unite(modis_burn_idn, burn_day, burn_day1:burn_day19, sep = ",", na.rm = TRUE) %>% mutate(burn_day = str_replace_all(burn_day, 'NA,?', ''))
modis_burn_idn_clean <- unite(modis_burn_idn_clean, burn_year, burn_year1:burn_year19, sep = ",", na.rm = TRUE) %>% mutate(burn_year = str_replace_all(burn_year, 'NA,?', ''))
'
# Cleaning up the value in moratorium column
modis_burn_idn$PIPPIB_15 <- ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_GAMBUT', 'Moratorium on Peatland',
                                   ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_KAWASAN', 'Moratorium on Watershed Protection Forest',
                                          ifelse(modis_burn_idn$PIPPIB_15 == 'MOR_PRIMER', 'Moratorium on Primary Forest', 'Outside Moratorium')))


# Filter NA then summarise
# not working
function(d) {
  subset(modis_burn_idn, !is.na(modis_burn_idn[[d]])) %>%
    select(ends_with(d), PIPPIB_15, area_ha) %>% 
    group_by(d, PIPPIB_15) %>% 
    summarise(hectare = sum(area_ha))
}


modis_burn_idn_2001 <- subset(modis_burn_idn, !is.na(burn_year1)) %>%
  select(burn_year1, PIPPIB_15, area_ha) %>% 
  group_by(burn_year1, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year1)

modis_burn_idn_2002 <- subset(modis_burn_idn, !is.na(burn_year2)) %>%
  select(burn_year2, PIPPIB_15, area_ha) %>% 
  group_by(burn_year2, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year2)

modis_burn_idn_2003 <- subset(modis_burn_idn, !is.na(burn_year3)) %>%
  select(burn_year3, PIPPIB_15, area_ha) %>% 
  group_by(burn_year3, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha))  %>%
  rename(burn_year = burn_year3)

modis_burn_idn_2004 <- subset(modis_burn_idn, !is.na(burn_year4)) %>%
  select(burn_year4, PIPPIB_15, area_ha) %>% 
  group_by(burn_year4, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year4)

modis_burn_idn_2005 <- subset(modis_burn_idn, !is.na(burn_year5)) %>%
  select(burn_year5, PIPPIB_15, area_ha) %>% 
  group_by(burn_year5, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year5)

modis_burn_idn_2006 <- subset(modis_burn_idn, !is.na(burn_year6)) %>%
  select(burn_year6, PIPPIB_15, area_ha) %>% 
  group_by(burn_year6, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year6)

modis_burn_idn_2007 <- subset(modis_burn_idn, !is.na(burn_year7)) %>%
  select(burn_year7, PIPPIB_15, area_ha) %>% 
  group_by(burn_year7, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year7)

modis_burn_idn_2008 <- subset(modis_burn_idn, !is.na(burn_year8)) %>%
  select(burn_year8, PIPPIB_15, area_ha) %>% 
  group_by(burn_year8, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year8)

modis_burn_idn_2009 <- subset(modis_burn_idn, !is.na(burn_year9)) %>%
  select(burn_year9, PIPPIB_15, area_ha) %>% 
  group_by(burn_year9, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year9)

modis_burn_idn_2010 <- subset(modis_burn_idn, !is.na(burn_year10)) %>%
  select(burn_year10, PIPPIB_15, area_ha) %>% 
  group_by(burn_year10, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year10)

modis_burn_idn_2011 <- subset(modis_burn_idn, !is.na(burn_year11)) %>%
  select(burn_year11, PIPPIB_15, area_ha) %>% 
  group_by(burn_year11, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year11)

modis_burn_idn_2012 <- subset(modis_burn_idn, !is.na(burn_year12)) %>%
  select(burn_year12, PIPPIB_15, area_ha) %>% 
  group_by(burn_year12, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year12)

modis_burn_idn_2013 <- subset(modis_burn_idn, !is.na(burn_year13)) %>%
  select(burn_year13, PIPPIB_15, area_ha) %>% 
  group_by(burn_year13, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year13)

modis_burn_idn_2014 <- subset(modis_burn_idn, !is.na(burn_year14)) %>%
  select(burn_year14, PIPPIB_15, area_ha) %>% 
  group_by(burn_year14, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year14)

modis_burn_idn_2015 <- subset(modis_burn_idn, !is.na(burn_year15)) %>%
  select(burn_year15, PIPPIB_15, area_ha) %>% 
  group_by(burn_year15, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year15)

modis_burn_idn_2016 <- subset(modis_burn_idn, !is.na(burn_year16)) %>%
  select(burn_year16, PIPPIB_15, area_ha) %>% 
  group_by(burn_year16, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year16)

modis_burn_idn_2017 <- subset(modis_burn_idn, !is.na(burn_year17)) %>%
  select(burn_year17, PIPPIB_15, area_ha) %>% 
  group_by(burn_year17, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year17)

modis_burn_idn_2018 <- subset(modis_burn_idn, !is.na(burn_year19)) %>%
  select(burn_year19, PIPPIB_15, area_ha) %>% 
  group_by(burn_year19, PIPPIB_15) %>% 
  summarise(hectare = sum(area_ha)) %>%
  rename(burn_year = burn_year19)


# merge multiple dataframes
modis_all <- Reduce(function(x, y) merge(x, y, all=TRUE), list(modis_burn_idn_2001, modis_burn_idn_2002, modis_burn_idn_2003, modis_burn_idn_2004, modis_burn_idn_2005, modis_burn_idn_2006, modis_burn_idn_2007, modis_burn_idn_2008, modis_burn_idn_2009, modis_burn_idn_2010, modis_burn_idn_2011, modis_burn_idn_2012, modis_burn_idn_2013, modis_burn_idn_2014, modis_burn_idn_2015, modis_burn_idn_2016, modis_burn_idn_2017, modis_burn_idn_2018))

# Cleaning the data
modis_burn_idn_clean$burn_day <- gsub(",$", "", modis_burn_idn_clean$burn_day)
modis_burn_idn_clean$burn_year <- gsub(",$", "", modis_burn_idn_clean$burn_year)
modis_burn_idn_clean$moratorium_status <- ifelse(modis_burn_idn_clean$PIPPIB_15 == 'MOR_GAMBUT', 'Moratorium on Peatland',
                                                 ifelse(modis_burn_idn_clean$PIPPIB_15 == 'MOR_KAWASAN', 'Moratorium on Watershed Protection Forest',
                                                        ifelse(modis_burn_idn_clean$PIPPIB_15 == 'MOR_PRIMER', 'Moratorium on Primary Forest', 'Outside Moratorium')))



write.xlsx(modis_all, file.path(out_dir, "Modis Burn Area Inside Moratorium.xlsx"), sheetName="Inside Outside Mor", showNA = FALSE)
