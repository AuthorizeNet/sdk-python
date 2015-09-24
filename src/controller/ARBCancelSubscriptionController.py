'''
Created on Jun 9, 2015

@author: egodolja
'''
from controller import APIOperationBase
from contract import binding
import logging

class ARBCancelSubscriptionController(APIOperationBase.APIOperationBase):
    
    def ARBCancelSubscriptionController(self, requestObject):
        if not requestObject.subscriptionId:
            logging.error('SubscriptionId Cannot be Null.')
            return 
        
        request = super(ARBCancelSubscriptionController, self).buildRequest('ARBCancelSubscriptionRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.ARBCancelSubscriptionResponse()