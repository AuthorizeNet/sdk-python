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

which perl > /dev/null
if [ $? -eq 0 ]
then
    echo Found perl
else
    echo Unable to find perl. Make sure perl is installed.
    exit 1
fi

which wget > /dev/null
if [ $? -eq 0 ]
then
    echo Found wget.Downloading AnetAPISchema file under Script directory.
	wget -O ./script/AnetApiSchema.xsd https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd
	if [ $? -eq 0 ]
	then
		echo AnetAPISchema.xsd downloaded.
	else
		echo Unable to download AnetAPISchema.
		exit 1
	fi
else
	which curl > /dev/null
	if [ $? -eq 0 ]
	then
		echo Found curl.Downloading AnetAPISchema file under Script directory.
		curl -o ./script/AnetApiSchema.xsd --noproxy '*' "https://apitest.authorize.net/xml/v1/schema/AnetApiSchema.xsd"
		if [ $? -eq 0 ]
		then
			echo AnetAPISchema.xsd downloaded
		else
			echo Unable to download AnetAPISchema.
			exit 1
		fi
	else
		echo Unable to find wget and curl. Make sure either one is installed
		exit 1
	fi
fi

LOCALXSDWITHANY=./script/AnetApiSchemaOut.xsd
CONTRACTSDIR=authorizenet
CONTRACTSFILE=apicontractsv1
PYXBGENPATH=`which pyxbgen`
TEMPFILE=binding

echo modifying XSD using perl to support backward compatibility
perl script/addany.pl script/AnetApiSchema.xsd script/IntermediateAnetOut.xsd script/AnetApiSchemaOut.xsd
if [ $? -eq 0 ]
then
	echo AnetOut.xsd generated 
else
    echo Unable to generate AnetOut.xsd
    exit 1
fi

echo Using pyxb from "${PYXBGENPATH}"
if [ -e "${TEMPFILE}.py" ]; then
    rm ${TEMPFILE}.py
fi

python "${PYXBGENPATH}" -u ${LOCALXSDWITHANY} -m ${TEMPFILE}
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