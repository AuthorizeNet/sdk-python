'''
Created on Sep 26, 2015

@author: krgupta
'''
import logging
from authorizenet.constants import constants
from authorizenet import apicontractsv1
from authorizenet import apicontrollersbase

        
class getTransactionDetailsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getTransactionDetailsController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseType(self):
        return self._responseType
#TODO        return apicontractsv1.getTransactionDetailsResponse()
    
