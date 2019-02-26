library(rgdal)

dir = "W:/GEORESEARCH/Deforestation/MoEF/Processing/wo plantation forest/forest_stock"
# Listing all files within directories
f <- list.files(dir, pattern = glob2rx("^forests*shp$"))

# names <- c("lc_prev", "lc_after", "prov", "island", "ha")

f = substr(f, 1, nchar(f) - 4)

year = c("2000", "2003", "2006", "2009", "2011", "2012", "2013","2014", "2015", "2016", "2017", "1990", "1996")
for (i in seq(1, length(f))) {
  x <- readOGR(dir, f[i])
  x@data["year"] <- year[i]
  writeOGR(x, dir, f[i], "ESRI Shapefile", overwrite_layer = T)
}