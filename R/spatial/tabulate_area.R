# Data Processing Library
library(foreign) # library for reading dbfs
library(dplyr)
library(magrittr)
library(tidyr)
library(ggplot2)
library(gridExtra) # arranging grid plots

# Spatial Package
library(raster)
library(rasterVis)
library(rgdal)

path = "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Social Forestry"
setwd(path)

## Tabulate Area by a region

tclpath <- paste(path, "tcl_sf_18.tif", sep="\\")
tcl.raw <- raster(tclpath)

tp <- plot(tcl.raw, axes=FALSE)

# Read the polygon data

sf_list <- c("Hutan Adat", "Hutan Desa", "Hutan Kemasyarakatan", "Hutan Tanaman Rakyat", "Izin Pemanfaatan Hutan Perhutanan Sosial", "Pengakuan dan Perlindungan Kemitraan Kehutanan")
sf_adm2 <- readOGR(dsn=path, layer="idn_sf_adm2")


# Plot the Social Forestry Extent
#sp <- ggplot() + geom_polygon(data=sf_adm2, aes(x=long, y=lat, group=group, fill=factor(type)),
                              #fill='cadetblue', color='black') +
  #theme_classic() +
  #coord_equal()


### Strip the plot of each social forestry schemes
#baseMap <- function(d, title="") {
  #ggplot() + geom_polygon(data=d, aes(x=long, y=lat, group=group)) +
    #ggtitle(title) +
    #theme_classic() +
    #coord_equal()
#}


# Function to tabulate tcl by region
tabFunc <- function(i, extracted, region, regname) {
  data <- as.data.frame(table(extracted[[i]]))
  data$name <- region[[regname]][[i]]
  return(data)
}

## need to revised the filtering year
populate_per_category <- function(t, c) {
    
    filtered_data <- subset(sf_adm2, (type == t & category == c))
    ## Extract tcl valeus by region social forestry schemes and tabulate
    ext.ha <- extract(tcl.raw, filtered_data, method = 'simple')

    # run through each region and compute a table of the count of raster cells by TCL. Produces a list
    tabs.ha <- lapply(seq(ext.ha), tabFunc, ext.ha, filtered_data, 'KABKOT')

    # Assemble into one dataframe
    tabs.ha <- do.call('rbind', tabs.ha)

    # Filtering the Year; Only 2001 - 2018 are selected
    tabs.ha$Var1 <- as.numeric(tabs.ha$Var1)
    tabs.ha %>% filter(tabs.ha$Var1 > 0, tabs.ha$Var1 < 20)

    sf <- filtered_data[!filtered_data$year %in% 0,]
    return(sf)
}



# Compare with ArcGIS's Tabulate Area tool


"
Tabulate Raster Area with R Reference
http://zevross.com/blog/2015/03/30/map-and-analyze-raster-data-in-r/
"