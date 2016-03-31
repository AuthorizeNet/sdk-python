'''
Created on March 30, 2016

@author: krgupta
'''
from authorizenet import apicontractsv1
from authorizenet import constants
from decimal import *
from authorizenet.apicontractsv1 import CTD_ANON
#from controller.CreateTransactionController import CreateTransactionController
from authorizenet.apicontrollers import *
from ConfigParser import SafeConfigParser
import datetime
from tests import apitestbase
#from tests import *
import os
import unittest
from authorizenet import apicontractsv1
#from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController
from tests import apitestbase
from authorizenet.apicontrollers import *
import test
from authorizenet import utility
import pyxb
import xml.dom.minidom
import datetime

class test_CreateTransactionUnitTest(apitestbase.ApiTestBase):

    def testPyxbDeserialization(self):
            self.__PyxbDeserialization(False, False)
    def testPyxbDeserializationIgnoreValidation(self):
            self.__PyxbDeserialization(False, True)
    def testPyxbDeserializationAtLast(self):
            self.__PyxbDeserialization(True, False)
    def testPyxbDeserializationIgnoreValidationAtLast(self):
            self.__PyxbDeserialization(True, True)
                          
    def __PyxbDeserialization(self, lastElement, ignoreValidation):
        loggingfilename = utility.helper.getproperty(constants.propertiesloggingfilename)
        logginglevel = utility.helper.getproperty(constants.propertiesexecutionlogginglevel)
        
        if (None == loggingfilename):
            loggingfilename = constants.defaultLogFileName
        if (None == logginglevel):
            logginglevel = constants.defaultLoggingLevel
            
        logging.basicConfig(filename=loggingfilename, level=logginglevel, format=constants.defaultlogformat)
          
        merchantAuth = apicontractsv1.merchantAuthenticationType()
        merchantAuth.name = "unknown"
        merchantAuth.transactionKey = "anon"
    
        creditCard = apicontractsv1.creditCardType()
        creditCard.cardNumber = "4111111111111111"
        creditCard.expirationDate = "2020-12"
    
        payment = apicontractsv1.paymentType()
        payment.creditCard = creditCard
    
        transactionrequest = apicontractsv1.transactionRequestType()
        transactionrequest.transactionType = "authCaptureTransaction"
        transactionrequest.amount = Decimal( 7.1)
        transactionrequest.payment = payment
    
        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = merchantAuth
        createtransactionrequest.transactionRequest = transactionrequest
        createtransactionrequest.refId = "MerchantID-0001"

        logging.debug( "Request: %s " % datetime.datetime.now())
        logging.debug( "       : %s " % createtransactionrequest )

        try:    
            xmlRequest = createtransactionrequest.toxml(encoding=constants.xml_encoding, element_name='createTransactionRequest')
            logging.debug( "Xml Request: %s" % xmlRequest)
        except Exception as ex:
            logging.debug( "Xml Exception: %s" % ex)
        
        if (lastElement == False): 
            splitString = "<ns1:amount>"
            lines = xmlRequest.split( splitString)
            badXmlElement = "<ns1:badElement>BadElement</ns1:badElement>"
            badXmlRequest = lines[0] + badXmlElement + splitString + lines[1]
            logging.debug( "Bad XmlRequest: %s" % badXmlRequest)
        
        else:
            splitStringAtLast = "</ns1:payment>"
            lines = xmlRequest.split( splitStringAtLast)
            badXmlElementAtLast = "<badElementAtLast>BadElementAtLast</badElementAtLast>"
            badXmlRequest = lines[0] + badXmlElementAtLast + splitStringAtLast + lines[1]
            logging.debug( "Bad XmlRequest at Last: %s" % badXmlRequest)
           
       
        if (ignoreValidation):
            pyxb.RequireValidWhenParsing(True)
        else:     
            pyxb.RequireValidWhenParsing(False)
        
        logging.debug( "Validation %s" % ignoreValidation)
        badDomXml = None
        try:
            deserializedBadRequest = xml.dom.minidom.parseString(badXmlRequest)
            logging.debug( "Dom Request: %s " % deserializedBadRequest )
            badDomXml = deserializedBadRequest.toxml(encoding=constants.xml_encoding, element_name='createTransactionRequest')
            logging.debug( "Bad Dom Request: %s " % badDomXml )
        except Exception as ex:
            exStr = str(ex)
            logging.debug( "Dom Exception: %s " % exStr)
        
        self.assertIsNotNone(badDomXml, "Null BadDom Request")
        self.assertEqual(xmlRequest, badDomXml, "BadDom does not match XmlRequest")
     
if __name__ =='__main__':
    unittest.main()  
