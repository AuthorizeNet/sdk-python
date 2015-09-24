'''
Created on Sep 21, 2015

@author: krgupta
'''
from controller import APIOperationBase
from contract import binding
from constants import *
import logging

class getTransactionDetailsController(APIOperationBase.APIOperationBase):
    
    def __init__(self):
        return
    
    def validateRequest(self, requestObject):     
               
        request = super(getTransactionDetailsController, self).buildRequest('getTransactionDetailsRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.getTransactionDetailsResponse()
    
    