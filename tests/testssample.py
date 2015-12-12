'''
Created on Nov 16, 2015

@author: krgupta
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
import unittest
from authorizenet import apicontractsv1
#from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController
from tests import apitestbase
from authorizenet.apicontrollers import *
import test
from authorizenet import utility
from datetime import datetime

class test_ReadProperty(apitestbase.ApiTestBase):
    def testPropertyFromFile(self):
        login= utility.helper.getproperty("api_login_id")
        transactionkey = utility.helper.getproperty("transaction_key")
        self.assertIsNotNone(login)
        self.assertIsNotNone(transactionkey)
        
'''
class test_TransactionReportingUnitTest(apitestbase.ApiTestBase):
    def testGetTransactionDetails(self):
        
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId ='2244574222' #update valid transaction id
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode)   
'''
class test_RecurringBillingTest(apitestbase.ApiTestBase):
    '''
    def testCreateSubscription(self):
        
        createsubscriptionrequest = apicontractsv1.ARBCreateSubscriptionRequest()
        createsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
        createsubscriptionrequest.refId = 'Sample'
        createsubscriptionrequest.subscription = self.subscriptionOne
        arbcreatesubscriptioncontroller = ARBCreateSubscriptionController(createsubscriptionrequest)
        arbcreatesubscriptioncontroller.execute()
        response = arbcreatesubscriptioncontroller.getresponse()
        self.assertIsNotNone(response.subscriptionId)
        self.assertEquals('Ok', response.messages.resultCode) 
    '''    
    def testgetsubscription(self):
                
        getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
        getSubscription.merchantAuthentication = self.merchantAuthentication
        getSubscription.subscriptionId = "2952220" 
        getSubscriptionController = ARBGetSubscriptionController(getSubscription)
        getSubscriptionController.execute()
        response = getSubscriptionController.getresponse()
        self.assertIsNotNone(response.subscription.name)
        self.assertEquals('Ok', response.messages.resultCode) 
           
'''
    def testcancelSubscription(self):
        
        cancelsubscriptionrequest = apicontractsv1.ARBCancelSubscriptionRequest()
        cancelsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
        cancelsubscriptionrequest.refId = 'Sample'
        cancelsubscriptionrequest.subscriptionId = '2261331' #input valid subscriptionId
        cancelsubscriptioncontroller = ARBCancelSubscriptionController (cancelsubscriptionrequest)
        cancelsubscriptioncontroller.execute()  
        response = cancelsubscriptioncontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode)  
'''
'''            
class paymentTransactionUnitTest(apitestbase.ApiTestBase):
    def testauthCaputureTransaction(self):
        
        transactionrequesttype = apicontractsv1.transactionRequestType()
        transactionrequesttype.transactionType = "authCaptureTransaction"
        transactionrequesttype.amount = self.amount
        transactionrequesttype.payment = self.payment
        transactionrequesttype.order = self.order
        transactionrequesttype.customer = self.customerData
        transactionrequesttype.billTo = self.billTo
        
        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = self.merchantAuthentication
        createtransactionrequest.refId = self.ref_id
        createtransactionrequest.transactionRequest = transactionrequesttype
        createtransactioncontroller = createTransactionController(createtransactionrequest)
        createtransactioncontroller.execute()
        response = createtransactioncontroller.getresponse()
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)
        self.assertIsNot("0", response.transactionResponse.transId)
        
    def testauthOnlyContinueTransaction(self):      
        
        transactionrequesttype = apicontractsv1.transactionRequestType()
        transactionrequesttype.transactionType = "authCaptureTransaction"
        transactionrequesttype.amount = self.amount
        transactionrequesttype.payment = self.payment
        transactionrequesttype.order = self.order
        transactionrequesttype.customer = self.customerData
        transactionrequesttype.billTo = self.billTo
        
        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = self.merchantAuthentication
        createtransactionrequest.refId = self.ref_id
        createtransactionrequest.transactionRequest = transactionrequesttype
        createtransactioncontroller = createTransactionController(createtransactionrequest)
        createtransactioncontroller.execute()
        response = createtransactioncontroller.getresponse()
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)
        
'''        
        
