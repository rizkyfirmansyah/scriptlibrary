/*

https://gis.stackexchange.com/questions/9199/postgis-topologyexception-side-location-conflict-at-226-001-39-5158-whats-the

https://postgis.net/docs/ST_MakeValid.html


https://gis.stackexchange.com/questions/165151/postgis-update-multipolygon-with-st-makevalid-gives-error

https://gis.stackexchange.com/questions/281350/topologyexception-side-location-conflict?noredirect=1&lq=1
*/

-- GEOSIntersects: TopologyException: side location conflict

SELECT ST_IsValidReason(geom) FROM izin_kh;



update izin_kh_provinsi
set geom = st_multi(st_collectionextract(st_makevalid(geom),3))
where st_isvalid(geom) = false;