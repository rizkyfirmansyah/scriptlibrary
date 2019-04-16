::Turn of displaying the code on the screen
@echo off
setlocal EnableDelayedExpansion

REM Example command to run in the command box

FOR %%f in (frame*.png) do convert %%f logo.png -gravity southeast -geometry +200+390 -composite D:\Universe\%%f
echo DONE