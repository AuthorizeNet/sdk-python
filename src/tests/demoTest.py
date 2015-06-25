'''
Created on Jun 22, 2015

@author: egodolja
'''
from contract import binding
from controller.constants import *
from contract.binding import CTD_ANON
from controller.ARBCreateSubscriptionController import ARBCreateSubscriptionController
from controller.ARBGetSubscriptionStatusController import ARBGetSubscriptionStatusController
from controller.ARBCancelSubscriptionController import ARBCancelSubscriptionController
from decimal import *
import datetime

'''
1. Create a subscription
2. Get status of that subscription
3. Cancel subscription
4. Get status of cancelled subscription
'''
class demoTest():
    '''1. Create a subscription
            - create a createSubscription request object
            - create a createSubscripiton controller
            - build request
            - execute request
            - get subscriptionId from response to use in the following tests
    '''
    merchantAuthentication = binding.merchantAuthenticationType()
    merchantAuthentication.name = constants.CONST_API_LOGIN_ID
    merchantAuthentication.transactionKey = constants.CONST_TRANSACTION_KEY
    
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
    subscription.amount = Decimal('23.45')
    subscription.trialAmount = Decimal('0.01')
    subscription.payment = payment
    subscription.billTo = customerOne
    
    createSubscriptionRequest = binding.ARBCreateSubscriptionRequest()
    createSubscriptionRequest.merchantAuthentication = merchantAuthentication
    createSubscriptionRequest.refId = constants.CONST_REFID
    createSubscriptionRequest.subscription = subscription
    
    ARBCreateSubscriptionController = ARBCreateSubscriptionController()
    createRequest = ARBCreateSubscriptionController.ARBCreateSubscriptionController(createSubscriptionRequest)
    ARBCreateSubscriptionController.execute(createRequest, ARBCreateSubscriptionController.getResponseClass())
    subscriptionId = ARBCreateSubscriptionController.getSubscriptionIdFromResponse()
    
    '''2. Get subscription status
            - create a getSubscriptionStatus request object
            - use the subscriptionId from create subscription
            - create a getSubscriptionStatus controller
            - build request
            - execute request'''
    getSubscriptionStatusRequest = binding.ARBGetSubscriptionStatusRequest()
    getSubscriptionStatusRequest.merchantAuthentication = merchantAuthentication
    getSubscriptionStatusRequest.refId = constants.CONST_REFID
    getSubscriptionStatusRequest.subscriptionId = subscriptionId
    
    ARBGetSubscriptionStatusController = ARBGetSubscriptionStatusController()
    statusRequest = ARBGetSubscriptionStatusController.ARBGetSubscriptionStatusController(getSubscriptionStatusRequest)
    ARBGetSubscriptionStatusController.execute(statusRequest, ARBGetSubscriptionStatusController.getResponseClass())
    
    '''3. Cancel subscription
            - create a cancelSubscription request object
            - use the subscriptionId from create subscription
            - create a cancelSubscription controller
            - build request
            - execute request
    '''
    cancelSubscriptionRequest = binding.ARBCancelSubscriptionRequest()
    cancelSubscriptionRequest.merchantAuthentication = merchantAuthentication
    cancelSubscriptionRequest.refId = constants.CONST_REFID
    cancelSubscriptionRequest.subscriptionId = subscriptionId
    
    ARBCancelSubscriptionController = ARBCancelSubscriptionController()
    cancelRequest = ARBCancelSubscriptionController.ARBCancelSubscriptionController(cancelSubscriptionRequest)
    ARBCancelSubscriptionController.execute(cancelRequest, ARBCancelSubscriptionController.getResponseClass())
    
    '''4. Get subscription status
            - execute getSubscriptionStatus request from previously created request object
    '''
    ARBGetSubscriptionStatusController.execute(statusRequest, ARBGetSubscriptionStatusController.getResponseClass())
    
    
    
'''helper function to be added to ARBOperationBase for demoTest
    def getSubscriptionIdFromResponse(self,):
        order = binding.CreateFromDocument(response)
        return order.subscriptionId
'''

    
    
    
    