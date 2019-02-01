ogrinfo illog_2016.shp

cd D:/DATA
ogr2ogr -sql "SELECT ST_Centroid(geometry), * FROM illog_2016" -dialect sqlite illog_2016_centroid_4326.shp illog_2016.shp -t_srs EPSG:4326