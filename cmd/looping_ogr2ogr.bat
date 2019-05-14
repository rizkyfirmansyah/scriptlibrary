::Turn of displaying the code on the screen
@echo off
setlocal EnableDelayedExpansion

REM write output dir to a variable
REM %%~na tells the cmd to return only the filename without its extension
FOR /f "delims=" %%a in ('dir /b *.geojson') do ogr2ogr -f "GeoJSON" -sql "select *, CAST (LSKJUK AS float) from %%~na" "edited_%%a" %%a && echo "%%a DONE"

echo DONE