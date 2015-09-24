'''
Created on Jul 10, 2015

@author: egodolja
'''
from controller import APIOperationBase
from contract import binding
import logging


class CreateTransactionController(APIOperationBase.APIOperationBase):
    
    def CreateTransactionController(self, requestObject):
        #requestobject not none
        if not requestObject.transactionRequest:
            logging.error('transactionRequest Cannot be Null.')
            return 
        
        transactionType = requestObject.transactionRequest.transactionType
        
        if transactionType not in binding.transactionTypeEnum.values():
            logging.error('TransactionTypeEnum value is not valid')
            return
        
        request = super(CreateTransactionController, self).buildRequest('createTransactionRequest', requestObject)
        
        return request

    def getResponseClass(self):
        return binding.createTransactionResponse()