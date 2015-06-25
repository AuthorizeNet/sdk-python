@echo off
rem first script
echo current folder..
dir
echo going into pyxb folder..
cd PyxB-1.2.4
echo running pyxbgen on %DATE%-%TIME%
echo what is %TEMP%
set xsd=https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
rem !!Must have python already installed!!
python pyxbgen -u %xsd% -m bind
echo file is generated
Pause
