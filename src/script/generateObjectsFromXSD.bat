@echo off
echo running pyxbgen on %DATE%-%TIME%
set xsd=https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
set pyxbgenPath=C:\Users\egodolja\Documents\PyXB-1.2.4\
cd ..
cd contract
rem !!Must have python already installed!!
python "%pyxbgenPath%pyxbgen" -u %xsd% -m bind
echo file is generated
Pause
