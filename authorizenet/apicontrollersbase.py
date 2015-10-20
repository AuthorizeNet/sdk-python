'''
Created on Jul 6, 2015

@author: egodolja
'''
import abc
import logging
import os
import sys
import xml.dom.minidom

from pip._vendor import requests
from _pyio import __metaclass__
from ConfigParser import SafeConfigParser

from authorizenet.constants import constants
from authorizenet import apicontractsv1

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
    def getResponse(self):
        ''' Returns the de-serialized response'''
        pass
    
    @abc.abstractmethod
    def getResultCode(self):
        ''' Returns the result code from the response '''
        pass
    
    @abc.abstractmethod
    def getMessageType(self):
        ''' Returns the message type enum from the response '''
        pass

    @abc.abstractmethod
    def afterExecute(self):
        '''TODO'''
        pass

    @abc.abstractmethod
    def beforeExecute(self):
        '''TODO'''
        pass

class APIOperationBase(APIOperationBaseInterface):
    __metaclass__ = abc.ABCMeta
    
    parser = SafeConfigParser({"http":"","https":"","ftp":""})

    try:
        #if #TODO
        parser.read(os.path.dirname(__file__) + "/../properties.ini")
    except IOError, error:
        sys.exit( error)
    else:
        logFile = parser.get("properties", "logfilename")
        #TODO format and level in config file
        logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s %(message)s')
        endpoint = parser.get("properties", "sandbox")
    
    @abc.abstractmethod
    def validaterequest(self):
        return
    
    def validate(self):
        #add validation on merchant authentication #TODO
        #if ( "null" != authorizenet.apicontractsv1.merchantAuthenticationType.sessionToken)
        #    raise ValueError("SessionToken needs to be null")
        '''
        if ( "null" != apicontractsv1.merchantAuthenticationType.__password.value)
            raise ValueError('Password needs to be null')
        if ( null != merchantAuthenticationType.getMobileDeviceId()) 
            throw new IllegalArgumentException("MobileDeviceId needs to be null");
        ImpersonationAuthenticationType impersonationAuthenticationType = merchantAuthenticationType.getImpersonationAuthentication();
        if ( null != impersonationAuthenticationType) 
        throw new IllegalArgumentException("ImpersonationAuthenticationType needs to be null");
        '''
        self.validaterequest() 
        return     
    
    def _getRequest(self): #protected method
        return self._request 
     
    def buildRequest(self):
        logging.debug('building request..')
        #TODO requestType = type( self._request)
        requestType = self._requestType
        
        xmlRequest = self._request.toxml(encoding=constants.xml_encoding, element_name=requestType)
        #remove namespaces that toxml() generates
        xmlRequest = xmlRequest.replace(constants.nsNamespace1, '')
        xmlRequest = xmlRequest.replace(constants.nsNamespace2, '')
        
        return xmlRequest
    
    def getPrettyXmlRequest(self):
        xmlRequest = self.buildRequest()
        requestDom = xml.dom.minidom.parseString(xmlRequest)
        logging.debug('Request is: %s' % requestDom.toprettyxml())

        return requestDom
    
    def execute(self):
        logging.debug('Executing http post to url: %s', self.endpoint)
        
        self.beforeExecute()

        proxyDictionary = {'http' : self.parser.get("properties", "http"),
                            'https' : self.parser.get("properties" , "https"),
                            'ftp' : self.parser.get("properties", "ftp")}
        
        #requests is http request
        try:
            xmlRequest = self.buildRequest()
            self._httpResponse = requests.post(self.endpoint, data=xmlRequest, headers=constants.headers, proxies=proxyDictionary)
        except Exception as httpException:
            logging.error( 'Error retrieving http response from: %s for request: %s', self.endpoint, self.getPrettyXmlRequest())
            logging.error( 'Exception: %s, %s', type(httpException), httpException.args )


        if self._httpResponse:
            #encoding of response should be changed to retrieve text of response
            self._httpResponse.encoding = constants.response_encoding
            self._httpResponse = self._httpResponse.text[3:] #strip BOM
            self.afterExecute()
            try:
                self._response = apicontractsv1.CreateFromDocument(self._httpResponse)
            except Exception as createfromdocumentexception:
                logging.error( 'Create Document Exception: %s, %s', type(createfromdocumentexception), createfromdocumentexception.args )
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
    
    def getResponse(self):
        return self._response
    
    def getResultCode(self):
        if self._response:
            return self._response.resultCode
    
    def getMessageType(self):
        if self._response:
            return self._response.message
    
    def afterExecute(self ):
        return 
    
    def beforeExecute(self):
        return 
       
    def __init__(self, apiRequest, requestType):
        self._httpResponse = "null"
        self._request = "null"
        self._response = "null"
        self.__endpoint = "null"
        #TODO
        self._requestType = "null"
        
        if "null" == apiRequest:
            raise ValueError('Input request cannot be null')
        #TOdo null check for types
        
        self._request = apiRequest
        self._requestType = requestType
        self.validate()
            
        return
