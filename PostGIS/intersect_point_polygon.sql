-- ST_Within; Returns TRUE if the geom A is completely inside geom B

-- ST_Intersects; Returns TRUE if the geomteries "spatially intersect in 2D". Tolerance is 0.00001 meters

SELECT s.* FROM sebaran_or as s
INNER JOIN tambang as t
ON ST_Intersects(s.geom, t.geom);

-- You could query on ST_Within function also
SELECT s.* FROM sebaran_or as s
INNER JOIN tambang as t
ON ST_Within(s.geom, t.geom);


UPDATE sebaran_or
SET conflict = 'tambang'
WHERE gid IN (
SELECT s.gid FROM sebaran_or as s
INNER JOIN tambang as t
ON ST_Intersects(s.geom, t.geom));