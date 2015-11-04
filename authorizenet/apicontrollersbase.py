'''
Created on Nov 1, 2015

@author: krgupta
'''
import abc
import logging
import os
from os.path import expanduser

import sys
import xml.dom.minidom

from pip._vendor import requests
from _pyio import __metaclass__
from ConfigParser import SafeConfigParser
import ConfigParser

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
    
    parser = SafeConfigParser({"http":"","https":"","ftp":""})

   
    try:     
        home = os.path.expanduser("~")
        homedirpropertiesfilename = os.path.join(home, "anet_python_sdk_properties.ini")
        
        currdir = os.getcwd()
        currdirpropertiesfilename = os.path.join(currdir, "anet_python_sdk_properties.ini")
        
        if (os.path.exists(homedirpropertiesfilename)):
            parser.read(homedirpropertiesfilename)
        elif (os.path.exists(currdirpropertiesfilename)):
            parser.read(currdirpropertiesfilename)
        else :
            print "you do not have anet_python_sdk_properties.ini file neither in home nor in current working directory"
    except IOError, error:
        sys.exit( error)
    else:
        logFile = parser.get("properties", "logfilename")
        #TODO format and level in config file
        logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s %(message)s')
        endpoint = constants.SANDBOX_TESTMODE 
    
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
        logging.debug('Executing http post to url: %s', self.endpoint)
        
        self.beforeexecute()

        proxyDictionary = {'http' : self.parser.get("properties", "http"),
                            'https' : self.parser.get("properties" , "https"),
                            'ftp' : self.parser.get("properties", "ftp")}
        
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
    
    def getresponse(self):
        return self._response
    
    def getresultcode(self):
        if self._response:
            return self._response.resultCode
    
    def getmessagetype(self):
        if self._response:
            return self._response.message
    
    def afterexecute(self ):
        return 
    
    def beforeexecute(self):
        return 
       
    def __init__(self, apiRequest):
        self._httpResponse = "null"
        self._request = "null"
        self._response = "null"
        self.__endpoint = "null"
        
        if "null" == apiRequest:
            raise ValueError('Input request cannot be null')
        #TOdo null check for types
        
        self._request = apiRequest
        self.validate()
            
        return
