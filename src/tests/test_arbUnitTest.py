'''
Created on Jul 16, 2015

@author: egodolja
'''
from tests.ApiTestBase import ApiTestBase
from contract import binding
import unittest

from controller.ARBCreateSubscriptionController import ARBCreateSubscriptionController
from controller.ARBGetSubscriptionStatusController import ARBGetSubscriptionStatusController
from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController


class test_arbUnitTest(ApiTestBase):
    def setup(self):
        super(arbUnitTest, self).setUp()


    def createSubscription(self):
        global createSubscriptionController
        createSubscriptionRequest = binding.ARBCreateSubscriptionRequest()
        createSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        createSubscriptionRequest.refId = self.ref_id
        createSubscriptionRequest.subscription = self.subscriptionOne
        
        createSubscriptionController = ARBCreateSubscriptionController()
        createRequest = createSubscriptionController.ARBCreateSubscriptionController(createSubscriptionRequest)
        createSubscriptionController.execute(createRequest, createSubscriptionController.getResponseClass())
        
        response = createSubscriptionController.getResponseObject()

        self.assertIsNotNone(response.subscriptionId)
        self.assertEquals('Ok', response.messages.resultCode)
        return response.subscriptionId
    
    def testgetSubscriptionStatus(self):
        global getSubscriptionStatusController
        subscriptionId = self.createSubscription()
        getSubscriptionStatusRequest = binding.ARBGetSubscriptionStatusRequest()
        getSubscriptionStatusRequest.merchantAuthentication = self.merchantAuthentication
        getSubscriptionStatusRequest.refId = self.ref_id
        getSubscriptionStatusRequest.subscriptionId = subscriptionId
        
        getSubscriptionStatusController = ARBGetSubscriptionStatusController()
        statusRequest = getSubscriptionStatusController.ARBGetSubscriptionStatusController(getSubscriptionStatusRequest)
        getSubscriptionStatusController.execute(statusRequest, getSubscriptionStatusController.getResponseClass())
        
        response = getSubscriptionStatusController.getResponseObject()
        
        self.assertEquals('active', response.status)
    
    def testcancelSubscription(self):
        global cancelSubscriptionController
        subscriptionId = self.createSubscription()
        cancelSubscriptionRequest = binding.ARBCancelSubscriptionRequest()
        cancelSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        cancelSubscriptionRequest.refId = self.ref_id
        cancelSubscriptionRequest.subscriptionId = subscriptionId
        
        cancelSubscriptionController = ARBCancelSubscriptionController()
        cancelRequest = cancelSubscriptionController.ARBCancelSubscriptionController(cancelSubscriptionRequest)
        cancelSubscriptionController.execute(cancelRequest, cancelSubscriptionController.getResponseClass())
        
        response = cancelSubscriptionController.getResponseObject()
        
        self.assertEquals('Ok', response.messages.resultCode)
       
if __name__ == '__main__':
    unittest.main()
    