'''
Created on Jun 9, 2015

@author: egodolja
'''
from controller import ARBOperationBase
from contract import binding

class ARBCreateSubscriptionController(ARBOperationBase.ARBOperationBase):
    
    def ARBCreateSubscriptionController(self, requestObject):
        if not requestObject.subscription:
            return 'Subscription Cannot be Null'
        
        request = super(ARBCreateSubscriptionController, self).buildRequest('ARBCreateSubscriptionRequest', requestObject)
        
        return request
    
    def getResponseClass(self):
        return binding.ARBCreateSubscriptionResponse()

