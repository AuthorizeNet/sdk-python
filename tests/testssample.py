'''
Created on Nov 16, 2015

@author: krgupta
'''
from authorizenet import apicontractsv1
from authorizenet.constants import constants
from authorizenet.apicontractsv1 import CTD_ANON
from authorizenet.apicontrollers import *
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
    def testGetTransactionDetails(self):    
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId ='20000152262' #update valid transaction id
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode)    
        self.assertIsNotNone(response.transaction.payment.creditCard.cardNumber)  
         
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
        #print ("Test named 'testCreateSubscription' has response.subscriptionId = %s" %response.subscriptionId)
        self.assertIsNotNone(response.subscriptionId)
        self.assertEquals('Ok', response.messages.resultCode)
        self.__class__.createdSubscriptionId = response.subscriptionId
  
    def testgetsubscription(self):
        getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
        getSubscription.merchantAuthentication = self.merchantAuthentication
        getSubscription.subscriptionId = self.__class__.createdSubscriptionId #update valid subscription id 
        #getSubscription.subscriptionId = '3259321'
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
        #cancelsubscriptionrequest.subscriptionId = '3259308'
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
        
class pyxbBinding(apitestbase.ApiTestBase):
    def testCreateSubscription_DeSerialize(self):
        arbXMLrequest = '<?xml version="1.0" encoding="utf-8"?><ARBCreateSubscriptionResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd"><refId>Sample</refId><messages><resultCode>Ok</resultCode><message><code>I00001</code><text>Successful.</text></message></messages><subscriptionId>3263738</subscriptionId><profile><customerProfileId>40712423</customerProfileId><customerPaymentProfileId>36983905</customerPaymentProfileId></profile></ARBCreateSubscriptionResponse>'
        #print( "ARBCreateTransaction Request: %s \n" % arbXMLrequest )
        try:
            '''deserialize XML to object '''    
            deserializedObject = None
            deserializedObject = apicontractsv1.CreateFromDocument(arbXMLrequest)           
            self.assertIsNotNone(deserializedObject, "Null deserializedObject ")
    
            deseriaziedArbXmlRequest = deserializedObject.toxml(encoding=constants.xml_encoding, element_name='ARBCreateSubscriptionResponse') 
            deseriaziedArbXmlRequest = deseriaziedArbXmlRequest.replace(constants.nsNamespace1, '')
            deseriaziedArbXmlRequest = deseriaziedArbXmlRequest.replace(constants.nsNamespace2, '')
            logging.debug( "Good Dom Request: %s " % deseriaziedArbXmlRequest )
            #print( "ARB Dom Request: %s \n" % deseriaziedArbXmlRequest )
            #print("de-serialized successfully. ARBCreateTransaction \n ")
        except Exception as ex:
            #print("failed to de-serialized successfully. ARBCreateTransaction \n ")
            logging.error( 'Create Document Exception: %s, %s', type(ex), ex.args )        
            
#     def testCreateSubscription_missingElementStillAssertOk(self):    
#         createsubscriptionrequest = apicontractsv1.ARBCreateSubscriptionRequest()
#         createsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
#         #createsubscriptionrequest.refId = 'Sample'
#         #createsubscriptionrequest.subscription = self.subscriptionOne #required field
#         arbcreatesubscriptioncontroller = ARBCreateSubscriptionController(createsubscriptionrequest)
#         arbcreatesubscriptioncontroller.execute()
#         response = arbcreatesubscriptioncontroller.getresponse()
#         self.assertEquals('Ok', response.messages.resultCode)
                
#     def testCreateSubscription_withResponseIDValue(self):    
#         createsubscriptionrequest = apicontractsv1.ARBCreateSubscriptionRequest()
#         createsubscriptionrequest.merchantAuthentication = self.merchantAuthentication
#         createsubscriptionrequest.refId = 'Sample'
#         createsubscriptionrequest.subscription = self.subscriptionOne #required field
#         arbcreatesubscriptioncontroller = ARBCreateSubscriptionController(createsubscriptionrequest)
#         arbcreatesubscriptioncontroller.execute()
#         response = arbcreatesubscriptioncontroller.getresponse()
#         print ("Test named 'testCreateSubscription_withResponseIDValue' has response.subscriptionId = %s" %response.subscriptionId)
#         self.assertEquals('Ok', response.messages.resultCode) 

    def testGetTransactionDetails_AssertNestedField(self):     
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId = '20000152262' #update valid transaction id
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode) 
        self.assertIsNotNone(response.transaction.settleAmount)    
        self.assertIsNotNone(response.transaction.payment.creditCard.cardNumber)
        self.assertIsNotNone(response.transaction.customer.id)
        self.assertIsNotNone(response.transaction.billTo.company)
        self.assertIsNotNone(response.transaction.entryMethod)
        self.assertIsNotNone(response.transaction.order.invoiceNumber)     
        
    def testGetTransactionDetails_UserAddsInvalidPropertyWhichIsNOTInRequestObject(self):     
        gettransactiondetailsrequest = apicontractsv1.getTransactionDetailsRequest()
        gettransactiondetailsrequest.merchantAuthentication = self.merchantAuthentication
        gettransactiondetailsrequest.transId ='20000152262' #update valid transaction id
        gettransactiondetailsrequest.abc = ' ' #user adds any extra element 
        gettransactiondetailscontroller = getTransactionDetailsController(gettransactiondetailsrequest)
        gettransactiondetailscontroller.execute()
        response =  gettransactiondetailscontroller.getresponse()
        self.assertEquals('Ok', response.messages.resultCode) 
        self.assertIsNotNone(response.transaction.settleAmount)    
        self.assertIsNotNone(response.transaction.payment.creditCard.cardNumber)
        self.assertIsNotNone(response.transaction.customer.id)
        self.assertIsNotNone(response.transaction.billTo.company)
        self.assertIsNotNone(response.transaction.entryMethod)
        self.assertIsNotNone(response.transaction.order.invoiceNumber)
   
         
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
