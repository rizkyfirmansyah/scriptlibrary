CREATE TABLE izin_kh_provinsi AS (
	SELECT i.class, i.type, i.geom, ip.provinsi, ip.island FROM izin_kh i, indonesia_provinsi_big ip
	WHERE ST_Intersects(i.geom, ip.geom) AND i.geom && ip.geom -- to accelerate query process
	GROUP BY ip.provinsi, 1, 2, 3, 5
);
