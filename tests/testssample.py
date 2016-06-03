'''
Created on Nov 16, 2015

@author: krgupta
'''
from authorizenet import apicontractsv1
from authorizenet.constants import constants
from authorizenet.apicontractsv1 import CTD_ANON
from authorizenet.apicontrollers import *
from decimal import *
import random
import datetime
import unittest
from tests import apitestbase
from authorizenet import utility

class test_ReadProperty(apitestbase.ApiTestBase):
    def testPropertyFromFile(self):
        login= utility.helper.getproperty("api.login.id")
        transactionkey = utility.helper.getproperty("transaction.key")
        self.assertIsNotNone(login)
        self.assertIsNotNone(transactionkey)

class test_TransactionReportingUnitTest(apitestbase.ApiTestBase):
    createdTransId = None
    def charge_credit_card(self):
        creditCard = apicontractsv1.creditCardType()
        creditCard.cardNumber = "4111111111111111"
        creditCard.expirationDate = "2020-12"
        payment = apicontractsv1.paymentType()
        payment.creditCard = creditCard
        transactionrequest = apicontractsv1.transactionRequestType()
        transactionrequest.transactionType = "authCaptureTransaction"
        transactionrequest.amount = Decimal(str(round(random.random()*100, 2)))
        transactionrequest.payment = payment
        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = self.merchantAuthentication
        createtransactionrequest.refId = "MerchantID-0001"
        createtransactionrequest.transactionRequest = transactionrequest
        createtransactioncontroller = createTransactionController(createtransactionrequest)
        createtransactioncontroller.execute()
        response = createtransactioncontroller.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'transactionResponse') == True:
            if hasattr(response.transactionResponse, 'transId') == True:
                self.__class__.createdTransId = response.transactionResponse.transId
        
        
    def testGetTransactionDetails(self):    
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId =  '20000152262' #update valid transaction id
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
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
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'subscriptionId') == True:
            self.__class__.createdSubscriptionId = response.subscriptionId
  
    def testgetsubscription(self):
        getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
        getSubscription.merchantAuthentication = self.merchantAuthentication
        getSubscription.subscriptionId = str(self.__class__.createdSubscriptionId) #update valid subscription id 
        getSubscriptionController = ARBGetSubscriptionController(getSubscription)
        getSubscriptionController.execute()
        response = getSubscriptionController.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
    
    def testcancelSubscription(self):   
        cancelsubscriptionrequest = apicontractsv1.ARBCancelSubscriptionRequest()
        cancelsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
        cancelsubscriptionrequest.refId = 'Sample'
        cancelsubscriptionrequest.subscriptionId = str(self.__class__.createdSubscriptionId) #input valid subscriptionId
        cancelsubscriptioncontroller = ARBCancelSubscriptionController (cancelsubscriptionrequest)
        cancelsubscriptioncontroller.execute()  
        response = cancelsubscriptioncontroller.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
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
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'transactionResponse') == True:
            self.assertIsNotNone(response.transactionResponse)
            if hasattr(response.transactionResponse, 'transId') == True:    
                self.assertIsNotNone(response.transactionResponse.transId)
            
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
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'transactionResponse') == True:
            self.assertIsNotNone(response.transactionResponse)
            if hasattr(response.transactionResponse, 'transId') == True:    
                self.assertIsNotNone(response.transactionResponse.transId)

class getCustomerProfileAndgetCustomerShippingAddressUnitTest(apitestbase.ApiTestBase):
    createdShippingAddressId = None
    generatedCustomerProfileId = None
    def testcreate_customer_profile2(self):
        createCustomerProfile = apicontractsv1.createCustomerProfileRequest()
        createCustomerProfile.merchantAuthentication = self.merchantAuthentication
        createCustomerProfile.profile = apicontractsv1.customerProfileType('jdoe' + str(random.randint(0, 10000)), 'John2 Doe', 'jdoe@mail.com')
        controller = createCustomerProfileController(createCustomerProfile)
        controller.execute()
        response = controller.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'customerProfileId') == True: 
            self.__class__.generatedCustomerProfileId = str(response.customerProfileId)
            
    def testget_customer_profile(self):
        getCustomerProfile = apicontractsv1.getCustomerProfileRequest()
        getCustomerProfile.merchantAuthentication = self.merchantAuthentication
        getCustomerProfile.customerProfileId = self.__class__.generatedCustomerProfileId 
        controller = getCustomerProfileController(getCustomerProfile)
        controller.execute()
        response = controller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode)
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)

    def testcreate_customer_shipping_address(self):
        officeAddress = apicontractsv1.customerAddressType();
        officeAddress.firstName = "John"
        officeAddress.lastName = "Doe"
        officeAddress.address = "123 Main St."
        officeAddress.city = "Bellevue"
        officeAddress.state = "WA"
        officeAddress.zip = "98004"
        officeAddress.country = "USA"
        officeAddress.phoneNumber = "000-000-0000"
        shippingAddressRequest = apicontractsv1.createCustomerShippingAddressRequest()
        shippingAddressRequest.address = officeAddress
        shippingAddressRequest.customerProfileId = self.__class__.generatedCustomerProfileId
        shippingAddressRequest.merchantAuthentication = self.merchantAuthentication
        controller = createCustomerShippingAddressController(shippingAddressRequest)
        controller.execute()
        response = controller.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode) 
        if hasattr(response, 'customerAddressId') == True: 
            self.__class__.createdShippingAddressId = str(response.customerAddressId)
        
    def testget_customer_shipping_address(self):
        getShippingAddress = apicontractsv1.getCustomerShippingAddressRequest()
        getShippingAddress.merchantAuthentication = self.merchantAuthentication
        getShippingAddress.customerProfileId = self.__class__.generatedCustomerProfileId 
        getShippingAddress.customerAddressId = self.__class__.createdShippingAddressId
        getShippingAddressController = getCustomerShippingAddressController(getShippingAddress)
        getShippingAddressController.execute()
        response = getShippingAddressController.getresponse()
        if hasattr(response, 'messages') == True:
            if hasattr(response.messages, 'resultCode') == True:
                self.assertEquals('Ok', response.messages.resultCode)  

'''    
class test_ProductionURL(apitestbase.ApiTestBase):  
    #Tests will run only with production credentials
    
          
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
