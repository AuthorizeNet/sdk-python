'''
Created on Jul 13, 2015

@author: egodolja
'''
from contract import binding
from decimal import *
from controller.CreateTransactionController import CreateTransactionController
from ConfigParser import SafeConfigParser
import os

class paymentTransactionsSampleCode(object):
    
    parser = SafeConfigParser()
    parser.read(os.path.dirname(__file__) + "/../properties.ini")
    
    api_login_id = parser.get("properties", "api.login.id")
    transaction_key = parser.get("properties", "transaction.key")
    ref_id = 'Sample'

    merchantAuthentication = binding.merchantAuthenticationType()
    merchantAuthentication.name = api_login_id
    merchantAuthentication.transactionKey = transaction_key
    
    creditCardOne = binding.creditCardType()
    creditCardOne.cardNumber = '4111111111111111'
    creditCardOne.expirationDate = '2020-12'
    creditCardOne.cardCode = "999"
    payment = binding.paymentType()
    payment.creditCard = creditCardOne
    
    order = binding.orderType()
    order.invoiceNumber = "INV-12345"
    order.description = "Product Description"
    
    '''lineitem = binding.lineItemType()
    lineitem.itemId = "1"
    lineitem.name = "vase"
    lineitem.description = "Cannes logo"
    lineitem.quantity = Decimal("18")
    lineitem.unitPrice = Decimal("45.00")
    array = {lineitem}
    lineitems = binding.ArrayOfLineItem()
    lineitems.lineItem = array
    
    tax = binding.extendedAmountType()
    tax.amount = Decimal("4.26")
    tax.name = "level2 tax name"
    tax.description = "level2 tax"
    
    duty = binding.extendedAmountType()
    duty.amount = Decimal("8.55")
    duty.name = "duty name"
    duty.description = "duty description"

    shipping = binding.extendedAmountType()
    shipping.amount = Decimal("4.26")
    shipping.name = "level2 tax name"
    shipping.description = "level2 tax"'''
    
    customer = binding.customerDataType()
    customer.id = "99999456654"
    
    billTo = binding.customerAddressType()
    billTo.firstName = "Ellen"
    billTo.lastName = "Johnson"
    billTo.company = "Souveniropolis"
    billTo.address = "14 Main St"
    billTo.city = "Pecan Springs"
    billTo.state = "TX"
    billTo.zip = "44628"
    billTo.country = "USA"
    
    '''shipTo = binding.nameAndAddressType()
    shipTo.firstName = "China"
    shipTo.lastName = "Bayles"
    shipTo.company = "Thyme for Tea"
    shipTo.address ="12 Main St"
    shipTo.city = "Pecan Springs"
    shipTo.state ="TX"
    shipTo.zip = "44628"
    shipTo.country = "USA"
    
    setting = binding.settingType()
    setting.settingName = "testRequest"
    setting.settingValue = "false"
    arraySetting = {setting}
    transactionSetting = binding.ArrayOfSetting()
    transactionSetting.setting = arraySetting
    
    userFieldOne = binding.userField()
    userFieldOne.name = "MerchantDefinedFieldName1"
    userFieldOne.value_ = "MerchantDefinedFieldValue1"
    userFieldTwo = binding.userField()
    userFieldTwo.name = "favorite_color"
    userFieldTwo.value_ = "blue"
    arrayUserFields = {userFieldOne, userFieldTwo}
    userFields = binding.CTD_ANON_()
    userFields.userField = arrayUserFields'''
    
    transactionRequest = binding.transactionRequestType()
    transactionRequest.transactionType = "authCaptureTransaction"
    transactionRequest.amount = Decimal("6.44")
    transactionRequest.payment = payment
    transactionRequest.order = order
    #transactionRequest.lineItems = lineitems
    #transactionRequest.tax = tax
    #transactionRequest.duty = duty
    #transactionRequest.shipping = shipping
    #transactionRequest.poNumber = "456654"
    transactionRequest.customer = customer
    transactionRequest.billTo = billTo
    #transactionRequest.shipTo = shipTo
    #transactionRequest.customerIP = "192.168.1.1"
    #transactionRequest.transactionSettings = transactionSetting
    #transactionRequest.userFields = userFields
    
    createTransactionRequest = binding.createTransactionRequest()
    createTransactionRequest.merchantAuthentication = merchantAuthentication
    createTransactionRequest.refId = ref_id
    createTransactionRequest.transactionRequest = transactionRequest
    
    CreateTransactionController = CreateTransactionController()
    request = CreateTransactionController.CreateTransactionController(createTransactionRequest)
    CreateTransactionController.execute(request, CreateTransactionController.getResponseClass())
    
    response = CreateTransactionController.getResponseObject()
    
    if response:
        #messagecodeenum ok
        if response.messages.resultCode == 'Ok':
            result = response.transactionResponse
            if result.responseCode == '1':
                print result.responseCode
                print 'Successful Credit Card Transaction'
                print ('authCode: %s' % result.authCode)
                print ('transId: %s' % result.transId)
            else:
                #not none 
                print ('Failed transaction %s' % result.responseCode)
        else:
            #not none
            print ('Failed transaction %s' % response.messages.resultCode)
    
            
    print '------------------------------------------'