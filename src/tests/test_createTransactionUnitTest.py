'''
Created on Jul 17, 2015

@author: egodolja
'''
import unittest
from tests.ApiTestBase import ApiTestBase
from contract import binding
from controller.CreateTransactionController import CreateTransactionController


class paymentTransactionUnitTest(ApiTestBase):
    def setup(self):
        super(paymentTransactionUnitTest, self).setup()
    
    def testauthCaputureTransaction(self):
        global transactionController 
        
        transactionRequestType = binding.transactionRequestType()
        transactionRequestType.transactionType = "authCaptureTransaction"
        transactionRequestType.amount = self.amount
        transactionRequestType.payment = self.payment
        transactionRequestType.order = self.order
        transactionRequestType.customer = self.customerData
        transactionRequestType.billTo = self.billTo
        
        createTransactionRequest = binding.createTransactionRequest()
        createTransactionRequest.merchantAuthentication = self.merchantAuthentication
        createTransactionRequest.refId = self.ref_id
        createTransactionRequest.transactionRequest = transactionRequestType
        
        transactionController = CreateTransactionController()
        transactionRequest = transactionController.CreateTransactionController(createTransactionRequest)
        transactionController.execute(transactionRequest, transactionController.getResponseClass())
        
        response = transactionController.getResponseObject()
        
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)
        self.assertIsNot("0", response.transactionResponse.transId)
    
    def testauthOnlyContinueTransaction(self):
        global transactionController
        
        transactionRequestType = binding.transactionRequestType()
        transactionRequestType.transactionType = "authOnlyTransaction"
        transactionRequestType.amount = self.amount
        transactionRequestType.payment = self.payment
        transactionRequestType.order = self.order
        transactionRequestType.customer = self.customerData
        transactionRequestType.billTo = self.billTo
        
        createTransactionRequest = binding.createTransactionRequest()
        createTransactionRequest.merchantAuthentication = self.merchantAuthentication
        createTransactionRequest.refId = self.ref_id
        createTransactionRequest.transactionRequest = transactionRequestType
        
        transactionController = CreateTransactionController()
        transactionRequest = transactionController.CreateTransactionController(createTransactionRequest)
        transactionController.execute(transactionRequest, transactionController.getResponseClass())
        
        response = transactionController.getResponseObject()
        self.assertIsNotNone(response.transactionResponse)
        self.assertIsNotNone(response.transactionResponse.transId)
    
    
if __name__ == "__main__":
    unittest.main()
    
    
