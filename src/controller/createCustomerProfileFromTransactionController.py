'''
Created on Sep 22, 2015

@author: krgupta
'''
from controller import APIOperationBase
from contract import binding
from constants import *
import logging


class createCustomerProfileFromTransactionController(APIOperationBase.APIOperationBase):
    
    def __init__(self):
        return
    
    def validateRequest(self, requestObject):  
        
        request = super(createCustomerProfileFromTransactionController, self).buildRequest('createCustomerProfileFromTransactionRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.createCustomerProfileResponse()
    