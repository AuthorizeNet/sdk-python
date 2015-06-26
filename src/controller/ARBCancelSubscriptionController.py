'''
Created on Jun 9, 2015

@author: egodolja
'''
from controller import ARBOperationBase
from contract import binding

class ARBCancelSubscriptionController(ARBOperationBase.ARBOperationBase):
    
    def ARBCancelSubscriptionController(self, requestObject):
        if not requestObject.subscriptionId:
            return 'SubscriptionId Cannot be Null'
        
        request = super(ARBCancelSubscriptionController, self).buildRequest('ARBCancelSubscriptionRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.ARBCancelSubscriptionResponse()