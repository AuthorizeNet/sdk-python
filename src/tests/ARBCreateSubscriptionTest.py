'''
Created on Jun 16, 2015

@author: egodolja
'''
from contract import binding
from controller.constants import *
from controller.ARBCreateSubscriptionController import ARBCreateSubscriptionController
from contract.binding import CTD_ANON
import datetime

class ARBCreateSubscriptionTest(object):
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
    
    subscription = binding.ARBSubscriptionType()
    subscription.paymentSchedule = paymentSchedule
    
    createSubscriptionRequest = binding.ARBCreateSubscriptionRequest()
    createSubscriptionRequest.merchantAuthentication = merchantAuthentication
    createSubscriptionRequest.refId = constants.CONST_REFID
    createSubscriptionRequest.subscription = subscription
    
    ARBCreateSubscriptionController = ARBCreateSubscriptionController()
    request = ARBCreateSubscriptionController.ARBCreateSubscriptionController(createSubscriptionRequest)
    ARBCreateSubscriptionController.execute(request, ARBCreateSubscriptionController.getResponseClass())
    
    