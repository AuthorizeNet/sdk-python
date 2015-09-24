'''
Created on Jul 6, 2015

@author: egodolja
'''
import abc

class APIOperationBaseInterface(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def buildRequest(self, requestType, requestObject):
        ''' Creates a request xml using type of request and request object'''
        return
    
    @abc.abstractmethod
    def execute(self, request, responseClass):
        ''' Makes a post call. Uses request xml and response class type to check 
                that the response was of correct type'''
        return
    
    @abc.abstractmethod
    def getResponseObject(self):
        ''' Returns the deserialized response object'''
        return
    
    @abc.abstractmethod
    def getResultCode(self):
        ''' Returns the result code from the response '''
        return
    
    @abc.abstractmethod
    def getMessageType(self):
        ''' Returns the message type enum from the response '''
        return

    @abc.abstractmethod
    def afterExecute(self, response):
        return
    