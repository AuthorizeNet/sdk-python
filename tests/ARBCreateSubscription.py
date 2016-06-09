import os, sys
import imp
from authorizenet import apicontractsv1
#from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from authorizenet import utility
from decimal import *
import datetime
import random
from authorizenet.constants import constants
import  pyxb
import xml.dom.minidom as dom
from lxml import objectify

def create_subscription():
    
    utility.helper.setpropertyfile('anet_python_sdk_properties.ini')
    
    #Setting details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = utility.helper.getproperty('api.login.id')
    merchantAuth.transactionKey = utility.helper.getproperty('transaction.key')
    
    dateOne = datetime.date(2020, 8, 30)

    paymentScheduleOne = apicontractsv1.paymentScheduleType()
    paymentScheduleOne.interval = apicontractsv1.paymentScheduleTypeInterval()
    
    paymentScheduleOne.interval.length = 1
    paymentScheduleOne.interval.unit = 'months'
    
    paymentScheduleOne.startDate = dateOne
    paymentScheduleOne.totalOccurrences = 12
    paymentScheduleOne.trialOccurrences = 1
    
    creditCardOne = apicontractsv1.creditCardType()
    creditCardOne.cardNumber = "4111111111111111"
    creditCardOne.expirationDate = "2020-12"
    
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCardOne
    
    customerOne = apicontractsv1.nameAndAddressType()
    customerOne.firstName = "John"
    customerOne.lastName = "Smith"
    
    customerData = apicontractsv1.customerDataType()
    customerData.id = "99999456654"

    order = apicontractsv1.orderType()
    order.invoiceNumber = "INV-21345"
    order.description = "Product description"
    
    billTo = apicontractsv1.customerAddressType()
    billTo.firstName = "Ellen"
    billTo.lastName = "Johnson"
    billTo.company = "Souveniropolis"
    billTo.address = "14 Main St"
    billTo.city = "Seattle"
    billTo.state = "WA"
    billTo.zip = "98122"
    billTo.country = "USA"

    # Setting subscription details
    subscription = apicontractsv1.ARBSubscriptionType()
    subscription.name = "Sample Subscription"
    subscription.paymentSchedule = paymentScheduleOne
    subscription.amount = Decimal(str(round(random.random()*100, 2)))
    subscription.trialAmount = Decimal('0.03')
    subscription.billTo = billTo
    subscription.payment = payment
    
    # Creating the request
    request = apicontractsv1.ARBCreateSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.subscription = subscription
    
    xmlRequest = request.toxml(encoding=constants.xml_encoding, element_name='createSubscriptionRequest')
    xmlRequest = xmlRequest.replace(constants.nsNamespace1, '')
    xmlRequest = xmlRequest.replace(constants.nsNamespace2, '') 
    print ("ARB request %s " %xmlRequest)
    
    # Creating and executing the controller
    controller = ARBCreateSubscriptionController(request)
    controller.execute()
    
    # Getting the response
    response = controller.getresponse()
    '''
    deseriaziedXmlResponse = response.toxml(encoding=constants.xml_encoding, element_name='createSubscriptionResponse') 
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace1, '')
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace2, '') 
    print( "ARB response: %s" % deseriaziedXmlResponse )
    '''
    print ("response.refId = %s" % response.refId)
    print ("response.subscriptionId = %s" % response.subscriptionId)
    print ("response.messages.resultCode = %s \n" %response.messages.resultCode)
    
#     itemDir = response.__dict__
#     for i in itemDir:
#         print '{0}  :  {1}'.format(i, itemDir[i])
    '''
    deseriaziedXmlResponse = response.toxml(encoding=constants.xml_encoding, element_name='createSubscriptionResponse') 
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace1, '')
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace2, '') 
    print( "ARB response: %s" % deseriaziedXmlResponse )
    print ("response.refId = %s" % response.refId)
    print ("response.subscriptionId = %s" % response.subscriptionId)
    print ("response.messages.resultCode = %s \n" %response.messages.resultCode)
    '''
    
    #krobject = dom.parse(deseriaziedXmlResponse) 
    
    #krobject = dom.parseString(deseriaziedXmlResponse)
    #print ("krobject.subscriptionId = %s" % krobject.subscriptionId)
    '''
    main = objectify.fromstring(deseriaziedXmlResponse)
    print ("main.subscriptionId = %s" % main.subscriptionId)
    print ("main.messages.resultCode = %s" %main.messages.resultCode)
    print ("main.profile.customerProfileId = %s \n" %main.profile.customerProfileId)
    '''
    #text = pyxb.six.u('').join(pyxb.NonElementContent(response))    
    #print("text = %s" %text)
    
#     uni = type(response)
#     print (" obj is %s" %uni)
    
    
#     x = pyxb.NonElementContent(response)
#     data = x.subscriptionId._Content__getValue
#     print("data = %s" %data)

if __name__ =='__main__':
    i = 0
    for i in range(1):
        print( "i: %s \n" %i )
        create_subscription()
        i += 1
    
