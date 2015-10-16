'''
Created on Jul 13, 2015

@author: egodolja
'''
from authorizenet import apicontractsv1
from decimal import *
from authorizenet.apicontractsv1 import CTD_ANON
#from controller.CreateTransactionController import CreateTransactionController
from authorizenet.apicontrollers import *
from ConfigParser import SafeConfigParser
import datetime
from tests import apitestbase
#from tests import *
import os


class test_arbUnitTest(apitestbase.ApiTestBase):
    def setup(self):
        super(test_arbUnitTest, self).setUp()

    def createSubscription(self):
        global createSubscriptionController
        createSubscriptionRequest = apicontractsv1.ARBCreateSubscriptionRequest()
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
        getSubscriptionStatusRequest = apicontractsv1.ARBGetSubscriptionStatusRequest()
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
        cancelSubscriptionRequest = apicontractsv1.ARBCancelSubscriptionRequest()
        cancelSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        cancelSubscriptionRequest.refId = self.ref_id
        cancelSubscriptionRequest.subscriptionId = subscriptionId
        
        cancelSubscriptionController = ARBCancelSubscriptionController()
        cancelRequest = cancelSubscriptionController.ARBCancelSubscriptionController(cancelSubscriptionRequest)
        cancelSubscriptionController.execute(cancelRequest, cancelSubscriptionController.getResponseClass())
        
        response = cancelSubscriptionController.getResponseObject()
        
        self.assertEquals('Ok', response.messages.resultCode)
        
class paymentTransactionUnitTest(apitestbase.ApiTestBase):
    def setup(self):
        super(paymentTransactionUnitTest, self).setup()
    
    def testauthCaputureTransaction(self):
        global transactionController 
        
        transactionRequestType = apicontractsv1.transactionRequestType()
        transactionRequestType.transactionType = "authCaptureTransaction"
        transactionRequestType.amount = self.amount
        transactionRequestType.payment = self.payment
        transactionRequestType.order = self.order
        transactionRequestType.customer = self.customerData
        transactionRequestType.billTo = self.billTo
        
        createTransactionRequest = apicontractsv1.createTransactionRequest()
        createTransactionRequest.merchantAuthentication = self.merchantAuthentication
        createTransactionRequest.refId = self.ref_id
        createTransactionRequest.transactionRequest = transactionRequestType
        
        transactionController = createTransactionController()
        transactionRequest = transactionController.CreateTransactionController(createTransactionRequest)
        transactionController.execute(transactionRequest, transactionController.getResponseClass())
        
        response = transactionController.getResponseObject()
        
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)
        self.assertIsNot("0", response.transactionResponse.transId)
    
    def testauthOnlyContinueTransaction(self):
        global transactionController
        
        transactionRequestType = apicontractsv1.transactionRequestType()
        transactionRequestType.transactionType = "authOnlyTransaction"
        transactionRequestType.amount = self.amount
        transactionRequestType.payment = self.payment
        transactionRequestType.order = self.order
        transactionRequestType.customer = self.customerData
        transactionRequestType.billTo = self.billTo
        
        createTransactionRequest = apicontractsv1.createTransactionRequest()
        createTransactionRequest.merchantAuthentication = self.merchantAuthentication
        createTransactionRequest.refId = self.ref_id
        createTransactionRequest.transactionRequest = transactionRequestType
        
        transactionController = createTransactionController()
        transactionRequest = transactionController.CreateTransactionController(createTransactionRequest)
        transactionController.execute(transactionRequest, transactionController.getResponseClass())
        
        response = transactionController.getResponseObject()
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)


