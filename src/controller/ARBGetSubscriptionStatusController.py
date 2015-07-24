'''
Created on Jun 9, 2015

@author: egodolja
'''
from controller import ARBOperationBase
from contract import binding
from constants import *
import logging


class ARBGetSubscriptionStatusController(ARBOperationBase.ARBOperationBase):
    
    def ARBGetSubscriptionStatusController(self, requestObject):
        if not requestObject.subscriptionId:
            logging.debug('SubscriptionId Cannot be Null.') 
            return
        
        request = super(ARBGetSubscriptionStatusController, self).buildRequest('ARBGetSubscriptionStatusRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.ARBGetSubscriptionStatusResponse()
    
    def afterExecute(self, response):
        if constants.StatusStart in response:
            response = response.replace(constants.note, '')
            start = response.index(constants.StatusStart)
            end = response.index(constants.StatusEnd)
            response = response.replace(response[start:end+9], '')
        return response
        