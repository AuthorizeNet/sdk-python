'''
Created on Jun 15, 2015

@author: egodolja
'''
from contract import binding
from controller.constants import *
from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController


class ARBCancelSubscriptionTest(object):
    merchantAuthentication = binding.merchantAuthenticationType()
    merchantAuthentication.name = constants.CONST_API_LOGIN_ID
    merchantAuthentication.transactionKey = constants.CONST_TRANSACTION_KEY
    cancelSubscriptionRequest = binding.ARBCancelSubscriptionRequest()
    cancelSubscriptionRequest.merchantAuthentication = merchantAuthentication
    cancelSubscriptionRequest.refId = 'Sample'
    cancelSubscriptionRequest.subscriptionId = '2582968'
    
    ARBCancelSubscriptionController = ARBCancelSubscriptionController()
    request =  ARBCancelSubscriptionController.ARBCancelSubscriptionController(cancelSubscriptionRequest)
    ARBCancelSubscriptionController.execute(request, ARBCancelSubscriptionController.getResponseClass())