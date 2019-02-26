library(tidyr)
library(dplyr)
library(sf)
library(ggplot2)
library(rgdal)

# Reading all the shp data
def_90_96 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_90_96.shp")
def_96_00 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_96_00.shp")
def_00_03 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_00_03.shp")
def_03_06 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_03_06.shp")
def_06_09 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_06_09.shp")
def_09_11 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_09_11.shp")
def_11_12 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_11_12.shp")
def_12_13 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_12_13.shp")
def_13_14 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_13_14.shp")
def_14_15 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_14_15.shp")
def_15_16 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_15_16.shp")
def_16_17 <- st_read("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/indoprov_def_16_17.shp")

# change the column names of each data
column <- c("lu_code_prev", "lu_code_after", "prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry")

colnames(def_90_96) <- column
colnames(def_96_00) <- column
colnames(def_00_03) <- column
colnames(def_03_06) <- column
colnames(def_06_09) <- column
colnames(def_09_11) <- column
colnames(def_11_12) <- column
colnames(def_12_13) <- column
colnames(def_13_14) <- column
colnames(def_14_15) <- column
colnames(def_15_16) <- column
colnames(def_16_17) <- column

# keep only selected columns
def_90_96 <- def_90_96[, which(names(def_90_96) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_96_00 <- def_96_00[, which(names(def_96_00) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_00_03 <- def_00_03[, which(names(def_00_03) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_03_06 <- def_03_06[, which(names(def_03_06) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_06_09 <- def_06_09[, which(names(def_06_09) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_09_11 <- def_09_11[, which(names(def_09_11) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_11_12 <- def_11_12[, which(names(def_11_12) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_12_13 <- def_12_13[, which(names(def_12_13) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_13_14 <- def_13_14[, which(names(def_13_14) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_14_15 <- def_14_15[, which(names(def_14_15) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_15_16 <- def_15_16[, which(names(def_15_16) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]
def_16_17 <- def_16_17[, which(names(def_16_17) %in% c("prov", "island", "ha", "lu_prev", "lu_after", "deforestation", "geometry"))]

# Merge all shape files in dataframe into one 
def_indonesia <- Reduce(merge, list(def_90_96, def_96_00, def_00_03, def_03_06, def_06_09, def_09_11, def_11_12, def_12_13, def_13_14, def_14_15, def_15_16, def_16_17)) 

