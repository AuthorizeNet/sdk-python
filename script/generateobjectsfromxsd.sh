#!/bin/bash

# Script to generate the python contract from XSD
# Requires pyxb module to be installed and available in path

dt=`date '+%m/%d/%Y %H:%M:%S'`
echo Starting pyxbgen on ${dt}
which python > /dev/null
if [ $? -eq 0 ]
then
    echo Found python
else
    echo Unable to find python. Make sure python is installed.
    exit 1
fi

which pyxbgen > /tmp/pyxbgenpath.txt
if [ $? -eq 0 ]
then
    echo Found pyxbgen
else
    echo Unable to find pyxbgen. Make sure pyxb package is installed.
    exit 1
fi

XSDPATH=https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
#XSDPATH=https://api.authorize.net/xml/v1/schema/AnetApiSchema.xsd
CONTRACTSDIR=authorizenet
CONTRACTSFILE=apicontractsv1
PYXBGENPATH=`which pyxbgen`
TEMPFILE=binding

echo Using pyxb from "${PYXBGENPATH}"
if [ -e "${TEMPFILE}.py" ]; then
    rm ${TEMPFILE}.py
fi

python "${PYXBGENPATH}" -u ${XSDPATH} -m ${TEMPFILE}
if [ $? -eq 0 ]
then
    if [ -e "${CONTRACTSDIR}/${CONTRACTSFILE}.old" ]
    then
        rm "${CONTRACTSDIR}/${CONTRACTSFILE}.old"
    fi
    if [ -e "${CONTRACTSDIR}/${CONTRACTSFILE}.py" ]
    then
        rm "${CONTRACTSDIR}/${CONTRACTSFILE}.py"
    fi
    mv "${TEMPFILE}.py" "${CONTRACTSDIR}/${CONTRACTSFILE}.py"
    echo Bindings have been successfully generated from XSD in the file "${CONTRACTSDIR}/${CONTRACTSFILE}.py"
    echo Old contracts have been moved to .old
else
    echo Error generating bindings from XSD. Review the errors and rerun the script.
    exit 1
fi

exit 0

