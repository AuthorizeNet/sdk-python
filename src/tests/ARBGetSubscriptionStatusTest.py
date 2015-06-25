'''
Created on Jun 15, 2015

@author: egodolja
'''
from contract import binding
from controller.constants import *
from controller.ARBGetSubscriptionStatusController import ARBGetSubscriptionStatusController

class ARBGetSubscriptionStatusTest(object):
    merchantAuthentication = binding.merchantAuthenticationType()
    merchantAuthentication.name = constants.CONST_API_LOGIN_ID
    merchantAuthentication.transactionKey = constants.CONST_TRANSACTION_KEY
    
    getSubscriptionStatusRequest = binding.ARBGetSubscriptionStatusRequest()
    getSubscriptionStatusRequest.merchantAuthentication = merchantAuthentication
    getSubscriptionStatusRequest.refId = 'Sample'
    getSubscriptionStatusRequest.subscriptionId = '2580111'
    
    
    ARBGetSubscriptionStatusController = ARBGetSubscriptionStatusController()
    request = ARBGetSubscriptionStatusController.ARBGetSubscriptionStatusController(getSubscriptionStatusRequest)
    ARBGetSubscriptionStatusController.execute(request, binding.ARBGetSubscriptionStatusResponse())
    