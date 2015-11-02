'''
Created on Jul 15, 2015

@author: egodolja
'''

import unittest
import os
from ConfigParser import SafeConfigParser
from authorizenet import apicontractsv1
from authorizenet.apicontractsv1 import CTD_ANON
import datetime
from decimal import *
import random
import test

class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.amount = str(round(random.random()*100, 2))
        parser = SafeConfigParser()
        home = os.path.expanduser("~")
        propertiesfilename = os.path.join(home, "anet_python_sdk_properties.ini")
        parser.read(propertiesfilename)
        
        self.api_login_id = parser.get("properties", "api.login.id")
        self.transaction_key = parser.get("properties", "transaction.key")
        self.ref_id = 'Sample'
        
        self.merchantAuthentication = apicontractsv1.merchantAuthenticationType()
        self.merchantAuthentication.name = self.api_login_id
        self.merchantAuthentication.transactionKey = self.transaction_key
        
        self.dateOne = datetime.date(2020, 8, 30)
        self.interval = CTD_ANON()
        self.interval.length = 1
        self.interval.unit = 'months'
        self.paymentScheduleOne = apicontractsv1.paymentScheduleType()
        self.paymentScheduleOne.interval = self.interval
        self.paymentScheduleOne.startDate = self.dateOne
        self.paymentScheduleOne.totalOccurrences = 12
        self.paymentScheduleOne.trialOccurrences = 1
        
        self.creditCardOne = apicontractsv1.creditCardType()
        self.creditCardOne.cardNumber = "4111111111111111"
        self.creditCardOne.expirationDate = "2020-12"
        
        self.payment = apicontractsv1.paymentType()
        self.payment.creditCard = self.creditCardOne
        
        self.customerOne = apicontractsv1.nameAndAddressType()
        self.customerOne.firstName = "John"
        self.customerOne.lastName = "Smith"
        
        self.customerData = apicontractsv1.customerDataType()
        self.customerData.id = "99999456654"
        
        self.subscriptionOne = apicontractsv1.ARBSubscriptionType()
        self.subscriptionOne.paymentSchedule = self.paymentScheduleOne
        self.subscriptionOne.amount = Decimal(self.amount)
        self.subscriptionOne.trialAmount = Decimal ('0.03')
        self.subscriptionOne.payment = self.payment
        self.subscriptionOne.billTo = self.customerOne
        
        self.order = apicontractsv1.orderType()
        self.order.invoiceNumber = "INV-21345"
        self.order.description = "Product description"
        
        self.billTo = apicontractsv1.customerAddressType()
        self.billTo.firstName = "Ellen"
        self.billTo.lastName = "Johnson"
        self.billTo.company = "Souveniropolis"
        self.billTo.address = "14 Main St"
        self.billTo.city = "Seattle"
        self.billTo.state = "WA"
        self.billTo.zip = "98122"
        self.billTo.country = "USA"
       
    
        