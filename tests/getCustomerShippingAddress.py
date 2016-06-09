import os, sys
import imp
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from authorizenet import utility
from decimal import *
import datetime
import random
from authorizenet.constants import constants
from lxml import objectify

def get_customer_shipping_address():
    utility.helper.setpropertyfile('anet_python_sdk_properties.ini')
    
    #Setting details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = utility.helper.getproperty('api.login.id')
    merchantAuth.transactionKey = utility.helper.getproperty('transaction.key')
    # create get shipping address request
    getShippingAddress = apicontractsv1.getCustomerShippingAddressRequest()
    getShippingAddress.merchantAuthentication = merchantAuth
    getShippingAddress.customerProfileId = '40812683'
    getShippingAddress.customerAddressId = '38558024'

    # Make the API call
    getShippingAddressController = getCustomerShippingAddressController(getShippingAddress)
    getShippingAddressController.execute()
    response = getShippingAddressController.getresponse()

    if response.messages.resultCode == "Ok":
        print "SUCCESS"
        if hasattr(response, 'address') == True:
            print "The address is"
            print response.address.firstName +" " + response.address.lastName
            print response.address.address
            print response.address.city
            print response.address.state
            print response.address.zip
            print response.address.country
        if not hasattr(response, 'subscriptionIds'):
            print ("no subscriptionIds attr in response")
        else:  
            if hasattr(response, 'subscriptionIds') == True:
                if hasattr(response.subscriptionIds, 'subscriptionId') == True:
                    print "list of subscriptionid:"
                    for subscriptionid in (response.subscriptionIds.subscriptionId):
                        print subscriptionid
    else:
        print "ERROR"
        print "Message code : %s " % response.messages.message[0].code
        print "Message text : %s " % response.messages.message[0].text

if __name__ =='__main__':
    i = 0
    for i in range(200):
        print( "i: %s \n" %i )
        get_customer_shipping_address()
        i += 1
    
