library(dplyr)
library(tidyr)
library(readxl)
library(stringr)

setwd("W:/GEORESEARCH/Deforestation/GFW - MoEF/Results")

# storing your all variables list of value forest loss. It's important for mapping to your district value later
fcl_06 <- read.csv("indo_forest_loss_0608.csv")
fcl_09 <- read.csv("indo_forest_loss_0910.csv")
fcl_11 <- read.csv("indo_forest_loss_11.csv")
fcl_12 <- read.csv("indo_forest_loss_12.csv")
fcl_13 <- read.csv("indo_forest_loss_13.csv")
fcl_14 <- read.csv("indo_forest_loss_14.csv")
fcl_15 <- read.csv("indo_forest_loss_15.csv")
fcl_16 <- read.csv("indo_forest_loss_16.csv")

# get all datasets within global environment and store to the list
# fcl_obj <- lapply(ls(), get) # only applicable if your datasets store in one directory

# getting all defined datasets with pattern
fcl_obj <- mget(ls(pattern = "fcl_[0-9]"))

# keep all values of your variables within merge by specifying "all = TRUE"
merge_common <- function(x, y) merge(x, y, all = TRUE)

# Combine the elements of a given vector with Reduce function
fcl_tidy <- gather(Reduce(merge_common, fcl_obj), "moef_year", "forest_description", -Value, -Count, -tcl_indonesia_20, -OBJECTID)

fcl_final <- fcl_tidy %>%
  select(-OBJECTID) %>%
  filter(!is.na(forest_description)) %>%
  mutate(forest_description = replace(forest_description, forest_description == 1, "Hutan Lahan Kering Primer")) %>%
  mutate(forest_description = replace(forest_description, forest_description == 2, "Hutan Lahan Kering Sekunder")) %>%
  mutate(forest_description = replace(forest_description, forest_description == 3, "Hutan Mangrove Primer")) %>%
  mutate(forest_description = replace(forest_description, forest_description == 4, "Hutan Rawa Primer")) %>%
  mutate(forest_description = replace(forest_description, forest_description == 5, "Hutan Mangrove Sekunder")) %>%
  mutate(forest_description = replace(forest_description, forest_description == 6, "Hutan Rawa Sekunder")) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2006", 2006)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2009", 2009)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2011", 2011)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2012", 2012)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2013", 2013)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2014", 2014)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2015", 2015)) %>%
  mutate(moef_year = replace(moef_year, moef_year == "forest_2016", 2016)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "6", 2006)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "7", 2007)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "8", 2008)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "9", 2009)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "10", 2010)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "11", 2011)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "12", 2012)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "13", 2013)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "14", 2014)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "15", 2015)) %>%
  mutate(tcl_indonesia_20 = replace(tcl_indonesia_20, tcl_indonesia_20 == "16", 2016)) %>%
  rename(tcl_year = tcl_indonesia_20) %>%
  arrange(desc(tcl_year))

# create a function to read, join and creating tidy format of datasets
fcl_func <- function(sh) {
  data <- read_xlsx("TCL - MoEF Deforestation 2006 - 2016_raw.xlsx", sheet = sh)
  data_merge <- left_join(data, fcl_final[, c("Value", "tcl_year", "forest_description")], by = c("VALUE" = "Value")) 
  data_tidy <- gather(data_merge, "district", "hectares", -VALUE, -tcl_year, -forest_description) %>%
              filter(hectares != 0)
  
  # replacing underscore character to space 
  data_tidy$district <- str_to_title(gsub('_', ' ', data_tidy$district))
  data_tidy$hectares <- data_tidy$hectares * 30 * 30 / 10000 # convert pixel counts into hectares
  colnames(data_tidy) <- c("FID", "Forest Loss Year", "Forest Type", "District", "Hectares")
  return(data_tidy)
}

fcl_jawa <- fcl_func("Jawa Bali")
fcl_kalimantan <- fcl_func("Kalimantan")
fcl_maluku <- fcl_func("Maluku")
fcl_nusa_tenggara <- fcl_func("Nusa Tenggara")
fcl_papua <- fcl_func("Papua")
fcl_sulawesi <- fcl_func("Sulawesi")
fcl_sumatera <- fcl_func("Sumatera")

write.csv(fcl_jawa, file = "kabkot_jawa.csv")
write.csv(fcl_kalimantan, file = "kabkot_kalimantan.csv")
write.csv(fcl_maluku, file = "kabkot_maluku.csv")
write.csv(fcl_nusa_tenggara, file = "kabkot_nusa_tenggara.csv")
write.csv(fcl_papua, file = "kabkot_papua.csv")
write.csv(fcl_sulawesi, file = "kabkot_sulawesi.csv")
write.csv(fcl_sumatera, file = "kabkot_sumatera.csv")

# rm(list = c("sumatera", "sumatera_merge", "sumatera_tidy","papua", "sulawesi", "nusa_tenggara", "maluku"))

