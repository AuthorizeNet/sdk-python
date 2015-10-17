@echo off
rem first script
echo current folder..
dir
echo running pyxbgen on %DATE%-%TIME%
set xsd=https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
set pyxbgenPath = C:\Users\egodolja\Documents\PyXB-1.2.4\scripts\
cd pyxbgenPath
echo --------------
dir
echo -----------------
rem !!Must have python already installed!!
python "%pyxbgenPath%pyxbgen" -u %xsd% -m bind
echo file is generated
Pause
