ogr2ogr -f "GeoJSON" -sql "select *, CAST(LSKJUK AS integer) from query_22000_24000" query_22000_24000_edited.geojson query_22000_24000.geojson

ogr2ogr -f "ESRI Shapefile" -sql "select *, CAST(LSKJUK AS integer) from kh_14000_14100" kh_14000_14100_edited.shp kh_14000_14100.shp

ogr2ogr -f "ESRI Shapefile" -sql "select *, CAST(TSKJUK AS float) from kh_14000_14100_edited" kh_14000_14100.shp kh_14000_14100_edited.shp