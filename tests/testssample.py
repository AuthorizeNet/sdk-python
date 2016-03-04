'''
Created on Nov 16, 2015

@author: krgupta
'''
from authorizenet import apicontractsv1
from authorizenet import constants
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
from authorizenet.apicontrollersbase import APIOperationBase

class test_ReadProperty(apitestbase.ApiTestBase):
    def testPropertyFromFile(self):
        login= utility.helper.getproperty("api.login.id")
        transactionkey = utility.helper.getproperty("transaction.key")
        self.assertIsNotNone(login)
        self.assertIsNotNone(transactionkey)
 
  
class test_TransactionReportingUnitTest(apitestbase.ApiTestBase):
    def testGetTransactionDetails(self):
        
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId ='2252271173' #update valid transaction id
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode) 

        
class test_RecurringBillingTest(apitestbase.ApiTestBase):

    createdSubscriptionId = None

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
        self.__class__.createdSubscriptionId = response.subscriptionId

       
    def testgetsubscription(self):
        
        getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
        getSubscription.merchantAuthentication = self.merchantAuthentication
        getSubscription.subscriptionId = self.__class__.createdSubscriptionId #update valid subscription id 
        getSubscriptionController = ARBGetSubscriptionController(getSubscription)
        getSubscriptionController.execute()
        response = getSubscriptionController.getresponse()
        self.assertIsNotNone(response.subscription.name)
        self.assertEquals('Ok', response.messages.resultCode) 
 
   
    def testcancelSubscription(self):
        
        cancelsubscriptionrequest = apicontractsv1.ARBCancelSubscriptionRequest()
        cancelsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
        cancelsubscriptionrequest.refId = 'Sample'
        cancelsubscriptionrequest.subscriptionId = self.__class__.createdSubscriptionId #input valid subscriptionId
        cancelsubscriptioncontroller = ARBCancelSubscriptionController (cancelsubscriptionrequest)
        cancelsubscriptioncontroller.execute()  
        response = cancelsubscriptioncontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode)  


class paymentTransactionUnitTest(apitestbase.ApiTestBase):
    
    def testauthCaptureTransaction(self):
        
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
class test_ProductionURL(apitestbase.ApiTestBase):  
    '' '' ''Tests will run only with production credentials
    '' '' ''
          
    def testGetSettledBatchList(self):
        settledBatchListRequest = apicontractsv1.getSettledBatchListRequest() 
        settledBatchListRequest.merchantAuthentication = self.merchantAuthentication
        settledBatchListController = getSettledBatchListController(settledBatchListRequest)
        customEndpoint = constants.PRODUCTION 
        apicontrollersbase.APIOperationBase.setenvironment(customEndpoint)
        settledBatchListController.execute() 
        response = settledBatchListController.getresponse() 
        self.assertEquals('Ok', response.messages.resultCode) 
    
    def testGetListofSubscriptions(self):    
        sorting = apicontractsv1.ARBGetSubscriptionListSorting()
        sorting.orderBy = apicontractsv1.ARBGetSubscriptionListOrderFieldEnum.id
        sorting.orderDescending = "false"
        paging = apicontractsv1.Paging()
        paging.limit = 1000
        paging.offset = 1
        GetListofSubscriptionRequest = apicontractsv1.ARBGetSubscriptionListRequest()
        GetListofSubscriptionRequest.merchantAuthentication = self.merchantAuthentication
        GetListofSubscriptionRequest.refId = "Sample"
        GetListofSubscriptionRequest.searchType = apicontractsv1.ARBGetSubscriptionListSearchTypeEnum.subscriptionInactive
        GetListofSubscriptionRequest.sorting = sorting
        GetListofSubscriptionRequest.paging = paging
        arbgetsubscriptionlistcontroller = ARBGetSubscriptionListController(GetListofSubscriptionRequest)
        customEndpoint = constants.PRODUCTION 
        apicontrollersbase.APIOperationBase.setenvironment(customEndpoint)
        arbgetsubscriptionlistcontroller.execute()
        response = arbgetsubscriptionlistcontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode) 
'''        
if __name__ =='__main__':
    unittest.main()  
