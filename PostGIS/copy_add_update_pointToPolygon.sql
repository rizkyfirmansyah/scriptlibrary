
-- Converting points geometry to rectangle polygons having a size of around 30m

CREATE TABLE idn_glad_logging AS (
SELECT gid, date, edition, ST_Envelope(ST_Buffer(geom, 0.000125)) AS geom
FROM idn_glad_points
 );

CREATE TABLE glad_2017 (

	long	double precision,
	lat		double precision,
	confidence	integer,
	year 		integer,
	julian_day	integer,
	area		double precision,
	emission	double precision,
	climate_mask	double precision
);

COPY glad_2017 FROM 'D:/The/Installer/se_asia_2017.csv' WITH CSV HEADER DELIMITER ',';


SELECT ST_Envelope(ST_Buffer(ST_SetSRID(ST_MakePoint(long, lat), 4326), 0.000125)) as geom
FROM glad_2017 LIMIT 100;
							 
ALTER TABLE glad_2017 ADD COLUMN geom geometry(Polygon, 4326);

ALTER TABLE glad_2017 ADD COLUMN id bigserial;

CREATE INDEX glad_2017_geom_idx
ON glad_2017
USING GIST(geom);

UPDATE glad_2017
SET id = DEFAULT;

-- Updating data and coverting points to polygon with 30x30m (Landsat pixels)
UPDATE glad_2017 g
SET geom = s.geom
FROM (SELECT id, ST_Envelope(ST_Buffer(ST_SetSRID(ST_MakePoint(long, lat), 4326), 0.000125)) as geom
FROM glad_2017) as s
WHERE g.id = s.id;

CREATE TABLE glad_2017_polygon AS (
SELECT id, long, lat, confidence, year, julian_day, ST_Envelope(ST_Buffer(ST_SetSRID(ST_MakePoint(long, lat), 4326), 0.000125)) AS geom
FROM glad_2017
 );

