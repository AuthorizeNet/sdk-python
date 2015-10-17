#!/bin/bash
currdir=`pwd`

dt=`date '+%m/%d/%Y %H:%M:%S'`
echo Starting ${dt}

cd ..
prevdir=`pwd`
#echo prevdirectory : ${prevdir}
cd ${currdir}
#echo currdir : ${currdir}

CDIR=${prevdir} 
echo "CDIR=$CDIR"   

SRCDIR=K:/sdk-python
GENFOLDER=authorizenet/apicontractsv1.py #Authorize.Net/Api/Contracts/V1 #
CONTROLLERFOLDER=controllerstemporary #Authorize.Net/Api/Controllers #
#CONTROLLERTMP=authorizenet #Authorize.Net/Api/ #

SRCLOG=${CDIR}/log/TestSources
CNTLOG=${CDIR}/log/TestControllers

if [ ! -e "${CDIR}/log" ]; then
	echo "Creating ${CDIR}/log"
	mkdir ${CDIR}/log
else
	echo "Deleting existing ${CDIR}/log/*"
	rm -rf ${CDIR}/log/*.* > /dev/null
fi

if [ ! -e "${SRCDIR}" ];then
	echo Unable to find "${SRCDIR}"
	exit 1
fi


echo Identifying Requests\/Responses to process from "${SRCDIR}"
#grep -i -e "request *=" -e "response *=" ${SRCDIR}/${GENFOLDER}/*.py | grep -v _AVS | cut -d= -f1 | egrep -v  "^ |\." | sort -u > ${SRCLOG}0.log
grep -i -e "request *=" -e "response *=" ${SRCDIR}/${GENFOLDER} | grep -v _AVS | cut -d= -f1 | egrep -v  "^ |\." | sort -u > ${SRCLOG}0.log

echo Getting Unique Request\/Responses
grep -i -e "request *$" -e "response *$" ${SRCLOG}0.log > ${SRCLOG}1.log

echo Identifying Object names
perl -pi -w -e 's/Request *$|Response *$//g;'  ${SRCLOG}1.log #------------------------evaluate
sort -u ${SRCLOG}1.log > ${SRCLOG}2.log

# Create backup for later comparison
cp ${SRCLOG}2.log ${SRCLOG}3.log >/dev/null

echo Creating Final List of Request\/Response to generate code
sort -u ${SRCLOG}2.log   > ${SRCLOG}.log

echo Creating Controllers
for cntrls in `cat ${SRCLOG}.log`  
do
    if [ -e "${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py" ]; then 
        echo ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py exists, Creating New
        #cp ${SRCDIR}/${CONTROLLERTMP}/ControllerTemplate.pyt ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.new
		cp ${SRCDIR}/ControllerTemplate.pyt ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.new
		perl -pi -w -e "s/APICONTROLLERNAME/$cntrls/g;" ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.new
    else
        echo Generating Code for ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py
        #cp ${SRCDIR}/${CONTROLLERTMP}/ControllerTemplate.pyt ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py
		cp ${SRCDIR}/ControllerTemplate.pyt ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py
		perl -pi -w -e "s/APICONTROLLERNAME/$cntrls/g;" ${SRCDIR}/${CONTROLLERFOLDER}/${cntrls}Controller.py
    fi
done


cat ${SRCDIR}/${CONTROLLERFOLDER}/*.py > ${SRCDIR}/${CONTROLLERFOLDER}/controllers.py
cat ${SRCDIR}/${CONTROLLERFOLDER}/header.py ${SRCDIR}/${CONTROLLERFOLDER}/controllers.py  > ${SRCDIR}/authorizenet/apicontrollers.py

echo FINISHED ${dt}
	 
