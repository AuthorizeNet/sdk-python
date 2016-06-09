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

def create_customerProfile():
    
    utility.helper.setpropertyfile('anet_python_sdk_properties.ini')
    
    #Setting details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = utility.helper.getproperty('api.login.id')
    merchantAuth.transactionKey = utility.helper.getproperty('transaction.key')
    
    createCustomerProfile = apicontractsv1.createCustomerProfileRequest()
    createCustomerProfile.merchantAuthentication = merchantAuth
    createCustomerProfile.profile = apicontractsv1.customerProfileType('jdoe' + str(random.randint(0, 10000)), 'John2 Doe', 'jdoe@mail.com')

    xmlRequest = createCustomerProfile.toxml(encoding=constants.xml_encoding, element_name='createCustomerProfile')
    xmlRequest = xmlRequest.replace(constants.nsNamespace1, '')
    xmlRequest = xmlRequest.replace(constants.nsNamespace2, '') 
    print ("Create Customer Profile request %s " %xmlRequest)
    
    # Creating and executing the controller
    controller = createCustomerProfileController(createCustomerProfile)
    controller.execute()

    # Getting the response
    response = controller.getresponse()

    print ("response.customerProfileId = %s" %response.customerProfileId)
    print ("response.messages.resultCode = %s \n" %response.messages.resultCode)
    
    '''
    deseriaziedXmlResponse = response.toxml(encoding=constants.xml_encoding, element_name='createCustomerProfileResponse') 
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace1, '')
    deseriaziedXmlResponse = deseriaziedXmlResponse.replace(constants.nsNamespace2, '') 
    print( "Create Customer Profile response: %s" % deseriaziedXmlResponse )
    print ("response.customerProfileId = %s" %response.customerProfileId)
    print ("response.messages.resultCode = %s \n" %response.messages.resultCode)
    '''
    '''
    main = objectify.fromstring(deseriaziedXmlResponse)
    print ("main.customerProfileId = %s" % main.customerProfileId)
    print ("main.messages.resultCode = %s \n" %main.messages.resultCode)
    #print ("main.profile.customerProfileId = %s \n" %main.profile.customerProfileId)
    '''


if __name__ =='__main__':
    i = 0
    for i in range(5):
        print( "i: %s \n" %i )
        create_customerProfile()
        i += 1
    
