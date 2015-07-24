'''
Created on Jun 1, 2015

@author: egodolja
'''
import abc
from ARBOperationBaseInterface import ARBOperationBaseInterface

from contract import binding
from pip._vendor import requests
from constants import *

import logging
import xml.dom.minidom
import os
from _pyio import __metaclass__
from ConfigParser import SafeConfigParser


class ARBOperationBase(ARBOperationBaseInterface):
    parser = SafeConfigParser()
    parser.read(os.path.dirname(__file__) + "/../properties.ini")
    logFile = parser.get("properties", "logfilename")
    
    logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s %(message)s')

    
    def buildRequest(self, requestType, requestObject):
        logging.debug('building request..')
        request = requestObject.toxml(encoding=constants.xml_encoding, element_name=requestType)

        #remove namespaces that toxml() generates
        request = request.replace(constants.nsNamespace1, '')
        request = request.replace(constants.nsNamespace2, '')
        
        xml_str = xml.dom.minidom.parseString(request)
        logging.debug('request is: %s' % xml_str.toprettyxml())
        return request
    
    
    def execute(self, request, responseClass):
        logging.debug('fetching response...')
        global responseObject
        global response
        
        request = self.beforeExecute(request)
        
        response = requests.post(constants.SANDBOX_TESTMODE, data=request, headers=constants.headers, proxies=constants.proxyDictionary)

        if response:

            #encoding of response should be changed to retrieve text of response
            response.encoding = constants.response_encoding
            response = response.text[3:] #strip BOM; check for amoutn of chars
            response = self.afterExecute(response)
            responseObject = binding.CreateFromDocument(response)

            if type(responseObject) == type(responseClass):
                xml_str = xml.dom.minidom.parseString(response)
                logging.debug('Received the following response: %s' % xml_str.toprettyxml())
            else:
                logging.debug('There was an error: %s' % request)
            #handle both errors: xsd validation, error codes
        else:
            print "Did not receive a response"
    
    def getResponseObject(self):
        return responseObject
    
    def getResultCode(self):
        if responseObject:
            return responseObject.resultCode
    
    def getMessageType(self):
        if responseObject:
            return responseObject.message
    
    def afterExecute(self, response):
        return response
    
    def beforeExecute(self, request):
        return request

    