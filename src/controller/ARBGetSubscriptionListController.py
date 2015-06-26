'''
Created on Jun 22, 2015

@author: egodolja
'''

from controller import ARBOperationBase
from contract import binding

class ARBGetSubscriptionListController(ARBOperationBase.ARBOperationBase):
    
    def ARBGetSubscriptionListController(self, requestObject):
        if not requestObject.searchType :
            return "searchType Cannot be Null"
        if not requestObject.paging :
            return "paging Cannot be Null"
        
        request = super(ARBGetSubscriptionListController, self).buildRequest('ARBGetSubscriptionListRequest', requestObject)
        
        return request
    
    def getResponseClass(self):
        return binding.ARBGetSubscriptionListResponse()