SELECT * FROM deforestation_umd as d
JOIN peatland as p
ON ST_Within(ST_Transform(d.geom, 3395), p.geom);


UPDATE deforestation_umd AS u
SET on_peatland = TRUE
FROM (
	SELECT d.id FROM deforestation_umd as d
	JOIN peatland as p
	ON ST_Within(ST_Transform(d.geom, 3395), p.geom)
    ) AS z
WHERE u.id = z.id;