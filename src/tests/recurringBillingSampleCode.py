'''
Created on Jun 22, 2015

@author: egodolja
'''
from contract import binding
from contract.binding import CTD_ANON
from controller.ARBCreateSubscriptionController import ARBCreateSubscriptionController
from controller.ARBGetSubscriptionStatusController import ARBGetSubscriptionStatusController
from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController
from decimal import *
import datetime
import os
from tests import ApiTestBase
from ConfigParser import SafeConfigParser

'''
1. Create a subscription
2. Get status of that subscription
3. Cancel subscription
4. Get status of cancelled subscription
'''
class recurringBillingSampleCode(ApiTestBase.ApiTestBase):
    
    '''1. Create a subscription
            - create a createSubscription request object
            - create a createSubscripiton controller
            - build request
            - execute request
            - get subscriptionId from response to use in the following tests
    '''
    parser = SafeConfigParser()
    parser.read( os.path.dirname(__file__) + "/../properties.ini")
        
    api_login_id = parser.get("properties", "api.login.id")
    transaction_key = parser.get("properties", "transaction.key")
    ref_Id = 'Sample'

    
    merchantAuthentication = binding.merchantAuthenticationType()
    merchantAuthentication.name = api_login_id
    merchantAuthentication.transactionKey = transaction_key
    
    dateOne = datetime.date(2020, 8, 30)
    interval = CTD_ANON()
    interval.length = 1
    interval.unit = 'months'
    paymentSchedule = binding.paymentScheduleType()
    paymentSchedule.interval = interval
    paymentSchedule.startDate = dateOne
    paymentSchedule.totalOccurrences = 12
    paymentSchedule.trialOccurrences = 1
    
    creditCardOne = binding.creditCardType()
    creditCardOne.cardNumber = '4111111111111111'
    creditCardOne.expirationDate = '2020-12'
    
    payment = binding.paymentType()
    payment.creditCard = creditCardOne
    
    customerOne = binding.nameAndAddressType()
    customerOne.firstName = 'John'
    customerOne.lastName = 'Smith'
    
    subscription = binding.ARBSubscriptionType()
    subscription.paymentSchedule = paymentSchedule
    subscription.amount = Decimal('13.55')
    subscription.trialAmount = Decimal('0.03')
    subscription.payment = payment
    subscription.billTo = customerOne
    
    createSubscriptionRequest = binding.ARBCreateSubscriptionRequest()
    createSubscriptionRequest.merchantAuthentication = merchantAuthentication
    createSubscriptionRequest.refId = ref_Id
    createSubscriptionRequest.subscription = subscription
    
    ARBCreateSubscriptionController = ARBCreateSubscriptionController()
    createRequest = ARBCreateSubscriptionController.ARBCreateSubscriptionController(createSubscriptionRequest)
    ARBCreateSubscriptionController.execute(createRequest, ARBCreateSubscriptionController.getResponseClass())
    
    createResponse = ARBCreateSubscriptionController.getResponseObject()
    
    subscriptionId = createResponse.subscriptionId
    if createResponse:
        if createResponse.messages.resultCode == 'Ok':
            #print createResponse.messages.message.text
            print 'Subscription successfully created.'
            print ('SubscriptionId: %s' % createResponse.subscriptionId)
            subscriptionId = createResponse.subscriptionId
        else:
            print ('Failed %s' % createResponse.messages.message)
    else:
        print ('Failed request')
    
    print '------------------------------------------'
    
    '''2. Get subscription status
        - create a getSubscriptionStatus request object
            - use the subscriptionId from create subscription
            - create a getSubscriptionStatus controller
            - build request
        - execute request'''
    getSubscriptionStatusRequest = binding.ARBGetSubscriptionStatusRequest()
    getSubscriptionStatusRequest.merchantAuthentication = merchantAuthentication
    getSubscriptionStatusRequest.refId = ref_Id
    getSubscriptionStatusRequest.subscriptionId = subscriptionId
    
    ARBGetSubscriptionStatusController = ARBGetSubscriptionStatusController()
    statusRequest = ARBGetSubscriptionStatusController.ARBGetSubscriptionStatusController(getSubscriptionStatusRequest)
    ARBGetSubscriptionStatusController.execute(statusRequest, ARBGetSubscriptionStatusController.getResponseClass())
    
    statusResponse = ARBCreateSubscriptionController.getResponseObject()
    
    if statusResponse:
        if statusResponse.messages.resultCode == 'Ok':
            #print statusResponse.messages.message.Text
            print 'Successful.'
            print ("Status: %s" % statusResponse.status)
        else:
            print ('Failed %s' % statusResponse.messages.resultCode)
    else:
        print 'Failed request'
    
    print '------------------------------------------'
    '''3. Cancel subscription
            - create a cancelSubscription request object
            - use the subscriptionId from create subscription
            - create a cancelSubscription controller
            - build request
            - execute request
    '''
    cancelSubscriptionRequest = binding.ARBCancelSubscriptionRequest()
    cancelSubscriptionRequest.merchantAuthentication = merchantAuthentication
    cancelSubscriptionRequest.refId = ref_Id
    cancelSubscriptionRequest.subscriptionId = subscriptionId
    
    ARBCancelSubscriptionController = ARBCancelSubscriptionController()
    cancelRequest = ARBCancelSubscriptionController.ARBCancelSubscriptionController(cancelSubscriptionRequest)
    ARBCancelSubscriptionController.execute(cancelRequest, ARBCancelSubscriptionController.getResponseClass())
    
    cancelResponse = ARBCancelSubscriptionController.getResponseObject()
    
    if cancelResponse:
        if cancelResponse.messages.resultCode == 'Ok':
            #print cancelResponse.messages.message.text
            print 'Subscription successfully cancelled.'
        else:
            print ('Failed %s' % cancelResponse.messages.resultCode)
    else:
        print 'Failed request'
        
    print '------------------------------------------'
    '''4. Get subscription status
            - execute getSubscriptionStatus request from previously created request object
    '''
    ARBGetSubscriptionStatusController.execute(statusRequest, ARBGetSubscriptionStatusController.getResponseClass())
    
    statusResponse = ARBGetSubscriptionStatusController.getResponseObject()
    
    if statusResponse:
        if statusResponse.messages.resultCode == 'Ok':
            #print statusResponse.messages.message.text
            print 'Successful.'
            print ("Status: %s" % statusResponse.status)
        else:
            print ('Failed %s' % statusResponse.messages.resultCode)
    else:
        print 'Failed request'
    
    print '------------------------------------------'