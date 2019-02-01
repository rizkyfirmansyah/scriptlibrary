pgsql2shp -f "D:/DATA/glad16_kph_unit16.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT * FROM glad16_kph_unit16"

pgsql2shp -f "D:/DATA/illog_2017_centroid.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT confidence, year, julian_day, ST_Centroid(geom) FROM illog_2017"