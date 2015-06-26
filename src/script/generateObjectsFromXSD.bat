@echo off
rem first script
rem !!!set pyxbgenFilePath = C:/.../pyxbgen!!!
set xsd=https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
rem !!Must have python already installed!!
python %pyxbgenFilePath% -u %xsd% -m bind
echo file is generated
Pause
