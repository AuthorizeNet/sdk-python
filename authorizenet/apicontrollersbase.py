'''
Created on Nov 1, 2015

@author: krgupta
'''
import abc
import logging
import pyxb
import xml.dom.minidom
from pip._vendor import requests
from _pyio import __metaclass__

from authorizenet.constants import constants
from authorizenet import apicontractsv1
from authorizenet import utility
'''
from authorizenet.apicontractsv1 import merchantAuthenticationType
from authorizenet.apicontractsv1 import ANetApiRequest
from authorizenet.apicontractsv1 import ANetApiResponse
'''
class APIOperationBaseInterface(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def execute(self):
        '''
        Makes a http-post call. 
        Uses request xml and response class type to check that the response was of correct type
        '''
        pass

    @abc.abstractmethod
    def getresponseclass(self):
        ''' Returns the response class '''
        pass
    
    @abc.abstractmethod
    def getrequesttype(self):
        ''' Returns the request class '''
        pass
    
    @abc.abstractmethod
    def getresponse(self):
        ''' Returns the de-serialized response'''
        pass
    
    @abc.abstractmethod
    def getresultcode(self):
        ''' Returns the result code from the response '''
        pass
    
    @abc.abstractmethod
    def getmessagetype(self):
        ''' Returns the message type enum from the response '''
        pass

    @abc.abstractmethod
    def afterexecute(self):
        '''Returns the message received from binding after processing request'''
        pass

    @abc.abstractmethod
    def beforeexecute(self):
        '''TODO'''
        pass

class APIOperationBase(APIOperationBaseInterface):
    __metaclass__ = abc.ABCMeta
        
    __initialized = False
    __merchantauthentication = "null"
    __environment = "null"

    @staticmethod
    def __classinitialized():
        return APIOperationBase.__initialized
    
    @abc.abstractmethod
    def validaterequest(self):
        return
    
    def validate(self):
        anetapirequest = self._getrequest()
        self.validateandsetmerchantauthentication()       
        self.validaterequest()
        
        return     
    
    def _getrequest(self): #protected method
        return self._request 
     
    def buildrequest(self):
        logging.debug('building request..')
        
        xmlRequest = self._request.toxml(encoding=constants.xml_encoding, element_name=self.getrequesttype())
        #remove namespaces that toxml() generates
        xmlRequest = xmlRequest.replace(constants.nsNamespace1, '')
        xmlRequest = xmlRequest.replace(constants.nsNamespace2, '')
        
        return xmlRequest
    
    def getprettyxmlrequest(self):
        xmlRequest = self.buildrequest()
        requestDom = xml.dom.minidom.parseString(xmlRequest)
        logging.debug('Request is: %s' % requestDom.toprettyxml())

        return requestDom
    
    def execute(self):
        
        self.endpoint = APIOperationBase.__environment
              
        logging.debug('Executing http post to url: %s', self.endpoint)
        
        self.beforeexecute()
        
        proxyDictionary = {'http' : utility.helper.getproperty("http"),
                           'https' : utility.helper.getproperty("https"),
                           'ftp' : utility.helper.getproperty("ftp")}
                           
        #requests is http request
        
        try:
            xmlRequest = self.buildrequest()
            self._httpResponse = requests.post(self.endpoint, data=xmlRequest, headers=constants.headers, proxies=proxyDictionary)
        except Exception as httpException:
            logging.error( 'Error retrieving http response from: %s for request: %s', self.endpoint, self.getprettyxmlrequest())
            logging.error( 'Exception: %s, %s', type(httpException), httpException.args )


        if self._httpResponse:
            #encoding of response should be changed to retrieve text of response
            self._httpResponse.encoding = constants.response_encoding
            self._httpResponse = self._httpResponse.text[3:] #strip BOM
            self.afterexecute()
            try:
                self._response = apicontractsv1.CreateFromDocument(self._httpResponse)
            except Exception as createfromdocumentexception:
                logging.error( 'Create Document Exception: %s, %s', type(createfromdocumentexception), createfromdocumentexception.args )
                pyxb.RequireValidWhenParsing(False)
                self._response = apicontractsv1.CreateFromDocument(self._httpResponse)
                pyxb.RequireValidWhenParsing(True)
            else:    
                if type(self.getresponseclass()) == type(self._response):
                    if self._response.messages.resultCode == "Error":
                        print "Response error"
            
                    domResponse = xml.dom.minidom.parseString(self._httpResponse)
                    logging.debug('Received response: %s' % domResponse.toprettyxml())
                else:
                    #Need to handle ErrorResponse 
                    logging.debug('Error retrieving response for request: %s' % self._request)
        else:
            print "Did not receive http response"
        return
    
    def getresponse(self):
        return self._response
    
    def getresultcode(self):
        resultcode = 'null'
        if self._response:
            resultcode = self._response.resultCode
        return resultcode
    
    def getmessagetype(self):
        message = 'null'
        if self._response:
            message = self._response.message
        return message
    
    def afterexecute(self ):
        return 
    
    def beforeexecute(self):
        return 
    
    @staticmethod
    def getmerchantauthentication(self):
        return self.__merchantauthentication
    
    @staticmethod
    def setmerchantauthentication(merchantauthentication):
        APIOperationBase.__merchantauthentication = merchantauthentication
        return
    
    def validateandsetmerchantauthentication(self):
        anetapirequest = apicontractsv1.ANetApiRequest()
        if (anetapirequest.merchantAuthentication == "null"):
            if (self.getmerchantauthentication() != "null"):
                anetapirequest.merchantAuthentication = self.getmerchantauthentication()
            else:
                raise ValueError('Merchant Authentication can not be null')
        return
    
    @staticmethod
    def getenvironment(self):
        return APIOperationBase.__environment
        
    
    @staticmethod
    def setenvironment(userenvironment):
        APIOperationBase.__environment = userenvironment 
        return 
    
    def __init__(self, apiRequest):
        self._httpResponse = None
        self._request = None
        self._response = None
               
        if None == apiRequest:
            raise ValueError('Input request cannot be null')
         
        self._request = apiRequest
        __merchantauthentication = apicontractsv1.merchantAuthenticationType()
        APIOperationBase.__environment = constants.SANDBOX
        
        APIOperationBase.setmerchantauthentication(__merchantauthentication)

        if ( False == APIOperationBase.__classinitialized()):
            loggingfilename = utility.helper.getproperty(constants.propertiesloggingfilename)
            logginglevel = utility.helper.getproperty(constants.propertiesexecutionlogginglevel)
            
            if (None == loggingfilename):
                loggingfilename = constants.defaultLogFileName
            if (None == logginglevel):
                logginglevel = constants.defaultLoggingLevel
                
            logging.basicConfig(filename=loggingfilename, level=logginglevel, format=constants.defaultlogformat)
            __initialized = True

        self.validate()
            
        return
