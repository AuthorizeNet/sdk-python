'''
Created on Jul 1, 2015

@author: egodolja
'''
import unittest

from mock import MagicMock
from contract import binding
from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController
from tests.ApiTestBase import ApiTestBase

class ARBCancelSubscriptionControllerTest(ApiTestBase):

    def test_ARBCancelSubscriptionController(self):
        cancelSubscriptionRequest = binding.ARBCancelSubscriptionRequest()
        cancelSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        cancelSubscriptionRequest.refId = 'Sample'
        cancelSubscriptionRequest.subscriptionId = '2680891'
        
        ctrl = ARBCancelSubscriptionController()

        ctrl.execute = MagicMock(return_value=None)
        #requests.post = MagicMock(return_value=None)

        cancelRequest = ctrl.ARBCancelSubscriptionController(cancelSubscriptionRequest)
        ctrl.execute(cancelRequest, binding.ARBCancelSubscriptionResponse)
        
        ctrl.execute.assert_called_with(cancelRequest, binding.ARBCancelSubscriptionResponse)
        ctrl.execute.assert_any_call(cancelRequest, binding.ARBCancelSubscriptionResponse)
        
if __name__ =='__main__':
    unittest.main()    