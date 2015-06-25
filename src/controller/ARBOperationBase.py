'''
Created on Jun 1, 2015

@author: egodolja
'''
from contract import binding

from pip._vendor import requests
from constants import *

import logging
import xml.dom.minidom


class ARBOperationBase(object):
    logging.basicConfig(filename='logFile.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

    
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
        global response
        response = requests.post(constants.SANDBOX_TESTMODE, data=request, headers=constants.headers, proxies=constants.proxyDictionary)
        
        #encoding of response should be changed to retrieve text of response
        response.encoding = constants.response_encoding
        if response:
            
            response = response.text[3:]
            if constants.StatusStart in response:
                response = response.replace(constants.note, '')
                response = self.afterExecuteStatus(response)
        
            order = binding.CreateFromDocument(response)
            
            if type(order) == type(responseClass):
                xml_str = xml.dom.minidom.parseString(response)
                logging.debug('Received the following response: %s' % xml_str.toprettyxml())
            else:
                logging.debug('There was an error: %s' % request)

    def afterExecuteStatus(self, response):
        start = response.index(constants.StatusStart)
        end = response.index(constants.StatusEnd)
        response = response.replace(response[start:end+9], '')
        return response