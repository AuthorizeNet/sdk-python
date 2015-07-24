'''
Created on Jun 15, 2015

@author: egodolja
'''
from contract import binding
from mock import MagicMock
import unittest
from controller.ARBGetSubscriptionStatusController import ARBGetSubscriptionStatusController

class ARBGetSubscriptionStatusTest(object):
    
    
    def testGetSubscriptionStatusController(self):
        getSubscriptionStatusRequest = binding.ARBGetSubscriptionStatusRequest()
        getSubscriptionStatusRequest.merchantAuthentication = self.merchantAuthentication
        getSubscriptionStatusRequest.refId = 'Sample'
        getSubscriptionStatusRequest.subscriptionId = '2680891'
    
        ctrl = ARBGetSubscriptionStatusController()
        
        ctrl.execute = MagicMock(return_value=None)
        
        statusRequest = ctrl.ARBGetSubscriptionStatusController(getSubscriptionStatusRequest)
        ctrl.execute(statusRequest, binding.ARBGetSubscriptionStatusResponse)
        
        ctrl.execute.assert_called_with(statusRequest, binding.ARBGetSubscriptionStatusResponse)
        ctrl.execute.assert_any_call(statusRequest, binding.ARBGetSubscriptionStatusResponse)

if __name__ == '__main__':
    unittest.main()