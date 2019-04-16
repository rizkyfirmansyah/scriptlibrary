pgsql2shp -f "D:/DATA/GEOSPATIAL/GFW/GLAD/glad_idn_2015.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT * FROM glad_idn_2015"

pgsql2shp -f "D:/DATA/GEOSPATIAL/GFW/GLAD/glad_idn_2016.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT g.* FROM glad_idn_2016 as g, papua_barat as p WHERE ST_Intersects(g.geom, p.geom)"

pgsql2shp -f "D:/DATA/GEOSPATIAL/GFW/GLAD/glad_idn_2017.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT * FROM glad_idn_2017"

pgsql2shp -f "D:/DATA/GEOSPATIAL/GFW/GLAD/glad_idn_2017.shp" -u postgres -h localhost -P WRIpass18! spatstat "SELECT confidence, date, ST_Centroid(geom) FROM glad_idn_2017"

