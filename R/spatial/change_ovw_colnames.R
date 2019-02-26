library(rgdal)
library(dplyr)

dir = "W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat"
# Listing all files within directories
f <- list.files(dir, pattern = "shp$")

names <- c("lc_prev", "lc_after", "prov", "island", "ha")

f = substr(f, 1, nchar(f) - 4)


## updating the specified values
lapply(f, function(i) {
  x <- readOGR(dir, i)
  
  colnames(x@data) <- names
 
  # convert your column to character 
  x@data$lc_after <- as.character(x@data$lc_after)
  # select your column with subset notation and use assign <-
  x@data$lc_after[x@data$lc_after == "Dry Rice Land Mixed with Scrub"] <- "Shrub-Mixed Dryland Farm"
  x@data$lc_after[x@data$lc_after == "Dry Rice Land"] <- "Dryland Agriculture"
  x@data$lc_after[x@data$lc_after == "Plantation"] <- "Estate Crop Plantation"
  x@data$lc_after[x@data$lc_after == "Mining"] <- "Open-pit Mining"
  x@data$lc_after[x@data$lc_after == "Rice Land"] <- "Rice Field"
  x@data$lc_after[x@data$lc_after == "Scrubland"] <- "Bush / Shrub"
  x@data$lc_after[x@data$lc_after == "Settlement"] <- "Settlement Area"
  x@data$lc_after[x@data$lc_after == "Swamp Scrubland"] <- "Swamp Shrub"
  x@data$lc_after[x@data$lc_after == "Water"] <- "Bodies of Water"
  x@data$lc_after[x@data$lc_after == "Transmigration"] <- "Transmigration Area"
  x@data$lc_after[x@data$lc_after == "Airport"] <- "Airport	/ Harbour"
  
  writeOGR(x, dir, i, "ESRI Shapefile", overwrite_layer = T)  
})



## read and overwrite column names on single file

x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat/indoprov_00_03_nonpeat.shp", "indoprov_00_03_nonpeat")
colnames(x@data) <- names
x@data["soil"] <- "nonpeat"
writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat/indoprov_00_03_nonpeat.shp", "indoprov_00_03_nonpeat", "ESRI Shapefile", overwrite_layer = T)

######

peat <- list.files("W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", pattern = "_peat.shp$")
nonpeat <- list.files("W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", pattern = "_nonpeat.shp$")

peat = substr(peat, 1, nchar(peat) - 4)
nonpeat = substr(nonpeat, 1, nchar(nonpeat) - 4)

## Adding new column and assigning value of peat
lapply(peat, function(i) {
  x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", i)
  x@data["soil"] <- "peat"
  
  writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", i, "ESRI Shapefile", overwrite_layer = T)  
})


## Adding new column and assigning value of nonpeat
lapply(nonpeat, function(i) {
  x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", i)
  x@data["soil"] <- "nonpeat"
  
  writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/w plantation forest/peat", i, "ESRI Shapefile", overwrite_layer = T)  
})


### Adding deforestation year on every single datasets
def_96_00 <- list.files("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", pattern = "_def_96_00")
def_96_00 = unique(substr(def_96_00, 1, nchar(def_96_00) - 4))

lapply(def_96_00, function(i) {
  x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i)
  x@data["def"] <- "1996 - 2000"
  
  writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i, "ESRI Shapefile", overwrite_layer = T)
})

def_00_03 <- list.files("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", pattern = "_def_00_03")
def_00_03 = unique(substr(def_00_03, 1, nchar(def_00_03) - 4))

lapply(def_00_03, function(i) {
  x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i)
  x@data["def"] <- "2000 - 2003"
  
  writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i, "ESRI Shapefile", overwrite_layer = T)
})

def_03_06 <- list.files("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", pattern = "_def_03_06")
def_03_06 = unique(substr(def_03_06, 1, nchar(def_03_06) - 4))

lapply(def_03_06, function(i) {
  x <- readOGR("W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i)
  x@data["def"] <- "2003 - 2006"
  
  writeOGR(x, "W:/GEORESEARCH/Deforestation/MoEF/Results/wo plantation forest/peat", i, "ESRI Shapefile", overwrite_layer = T)
})



