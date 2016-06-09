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

def get_customer_profile():
    utility.helper.setpropertyfile('anet_python_sdk_properties.ini')
    
    #Setting details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = utility.helper.getproperty('api.login.id')
    merchantAuth.transactionKey = utility.helper.getproperty('transaction.key')
    
    getCustomerProfile = apicontractsv1.getCustomerProfileRequest()
    getCustomerProfile.merchantAuthentication = merchantAuth
    getCustomerProfile.customerProfileId = '40812683'
    controller = getCustomerProfileController(getCustomerProfile)
    controller.execute()
 
    response = controller.getresponse()
 
    if (response.messages.resultCode=="Ok"):
        print "Successfully retrieved a customer with profile id %s and customer id %s" % (getCustomerProfile.customerProfileId, response.profile.merchantCustomerId)
        if hasattr(response, 'profile') == True:
            if hasattr(response.profile, 'paymentProfiles') == True:
                for paymentProfile in response.profile.paymentProfiles:
                     print ("paymentProfile in get_customerprofile is:" %paymentProfile)
                     print "Payment Profile ID %s" % str(paymentProfile.customerPaymentProfileId)
            if hasattr(response.profile, 'shipToList') == True:
                 for ship in response.profile.shipToList:
                     print "Shipping Details:"
                     print "First Name %s" % ship.firstName
                     print "Last Name %s" % ship.lastName
                     print "Address %s" % ship.address
                     print "Customer Address ID %s" % ship.customerAddressId
        if hasattr(response, 'subscriptionIds') == True:
            if hasattr(response.subscriptionIds, 'subscriptionId') == True:
                print "list of subscriptionid:"
                for subscriptionid in (response.subscriptionIds.subscriptionId):
                    print subscriptionid
    else:
        print "response code: %s" % response.messages.resultCode
        print "Failed to get customer profile information with id %s" % getCustomerProfile.customerProfileId

if __name__ =='__main__':
    i = 0
    for i in range(200):
        print( "i: %s \n" %i )
        get_customer_profile()
        i += 1
    
