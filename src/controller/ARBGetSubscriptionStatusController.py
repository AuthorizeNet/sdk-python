'''
Created on Jun 9, 2015

@author: egodolja
'''
from controller import ARBOperationBase
from contract import binding

class ARBGetSubscriptionStatusController(ARBOperationBase.ARBOperationBase):
    
    def ARBGetSubscriptionStatusController(self, requestObject):
        if not requestObject.subscriptionId: 
            return 'SubscriptionId cannot be null'
        
        request = super(ARBGetSubscriptionStatusController, self).buildRequest('ARBGetSubscriptionStatusRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.ARBGetSubscriptionStatusResponse()
