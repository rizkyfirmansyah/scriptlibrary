SELECT ST_Union(geom), SUM(ha) FROM deforest_00_03_nonpeat
WHERE pl00_id IN (2001, 2004, 2005);



CREATE TABLE deforest_non_peat AS
SELECT ST_Union(geom) as geom, SUM(ha) as ifl_deforest, '2000 - 2003' as year FROM deforest_00_03_nonpeat
WHERE pl00_id IN (2001, 2004, 2005);


INSERT INTO deforest_non_peat 
SELECT ST_Union(geom) as geom, SUM(ha) as ifl_deforest, '2006 - 2009' as year FROM deforest_06_09_nonpeat
WHERE pl06_id IN (2001, 2004, 2005);




