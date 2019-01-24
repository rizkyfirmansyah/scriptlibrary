-- Which way is faster?

-- https://postgis.net/2014/03/14/tip_intersection_faster/


-- https://gis.stackexchange.com/questions/253974/why-is-st-intersects-faster-than/253987

SELECT confidence, year, julian_day, g.geom FROM glad_asia_2017 as g, izin_kh_provinsi as k
WHERE ST_Within(g.geom, k.geom)
LIMIT 100;


--- file:///C:/Users/rizky/Downloads/Documents/Oscon2009_PostGISTips.pdf
CREATE TABLE illog_2017 AS (
	SELECT confidence, year, julian_day, g.geom FROM glad_asia_2017 as g, izin_kh_provinsi as k
	WHERE ST_Intersects(g.geom, k.geom)
);