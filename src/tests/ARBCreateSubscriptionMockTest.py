'''
Created on Jun 16, 2015

@author: egodolja
'''
from contract import binding
from controller.ARBCreateSubscriptionController import ARBCreateSubscriptionController
from tests.ApiTestBase import ApiTestBase
from mock import MagicMock
import unittest

class ARBCreateSubscriptionTest(ApiTestBase):

    def testCreateSubscriptionController(self):
        createSubscriptionRequest = binding.ARBCreateSubscriptionRequest()
        createSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        createSubscriptionRequest.refId = 'Sample'
        createSubscriptionRequest.subscription = self.subscriptionOne
    
        ctrl = ARBCreateSubscriptionController()
        
        ctrl.execute = MagicMock(return_value=None)
        
        createRequest = ctrl.ARBCreateSubscriptionController(createSubscriptionRequest)
        ctrl.execute(createRequest, binding.ARBCreateSubscriptionResponse)
        
        ctrl.execute.assert_called_with(createRequest, binding.ARBCreateSubscriptionResponse )
        ctrl.execute.assert_any_call(createRequest, binding.ARBCreateSubscriptionResponse)
        

if __name__ == '__main__':
    unittest.main()