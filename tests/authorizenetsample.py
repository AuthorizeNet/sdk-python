# from authorizenet.constants import constants
# from decimal import *
# import logging
# import random
# import datetime
# import unittest
# from authorizenet import utility
# import xml.dom.minidom
# from authorizenet import apicontractsv1
# 
# class pyxbBinding(unittest.TestCase):
#     merchantAuth = apicontractsv1.merchantAuthenticationType()
#     merchantAuth.name = "unknown"
#     merchantAuth.transactionKey = "anon"
#     
#     dateOne = datetime.date(2020, 8, 30)
#     
#     paymentScheduleOne = apicontractsv1.paymentScheduleType()
#     paymentScheduleOne.interval = apicontractsv1.paymentScheduleTypeInterval()
#         
#     paymentScheduleOne.interval.length = 1
#     paymentScheduleOne.interval.unit = 'months'
#         
#     paymentScheduleOne.startDate = dateOne
#     paymentScheduleOne.totalOccurrences = 12
#     paymentScheduleOne.trialOccurrences = 1
#     
#     creditCardOne = apicontractsv1.creditCardType()
#     creditCardOne.cardNumber = "4111111111111111"
#     creditCardOne.expirationDate = "2020-12"
#     
#     payment = apicontractsv1.paymentType()
#     payment.creditCard = creditCardOne
#         
#     customerOne = apicontractsv1.nameAndAddressType()
#     customerOne.firstName = "John"
#     customerOne.lastName = "Smith"
#     
#     subscriptionOne = apicontractsv1.ARBSubscriptionType()
#     subscriptionOne.paymentSchedule = paymentScheduleOne
#     subscriptionOne.amount = Decimal(str(round(random.random()*100, 2)))
#     subscriptionOne.trialAmount = Decimal ('0.03')
#     subscriptionOne.payment = payment
#     subscriptionOne.billTo = customerOne
#     
#     
#     def testCreateSubscription_DeSerialize(self):
#         createsubscriptionrequest = apicontractsv1.ARBCreateSubscriptionRequest()
#         createsubscriptionrequest.merchantAuthentication = self.merchantAuth
#         createsubscriptionrequest.refId = 'Sample'
#         createsubscriptionrequest.subscription = self.subscriptionOne
#         try:    
#             xmlRequest = createsubscriptionrequest.toxml(encoding=constants.xml_encoding, element_name='createsubscriptionrequest')
#             xmlRequest = xmlRequest.replace(constants.nsNamespace1, '')
#             xmlRequest = xmlRequest.replace(constants.nsNamespace2, '')   
#             print ("xmlRequest %s " %xmlRequest)
#             logging.debug( "Xml Request: %s" % xmlRequest)
#         except Exception as ex:
#             logging.debug( "Xml Exception: %s" % ex)
#         
#         try:
#             '''deserialize XML to object '''    
#             deserializedObject = None
#             deserializedObject = apicontractsv1.CreateFromDocument(xmlRequest)           
#             self.assertIsNotNone(deserializedObject, "Null deserializedObject ")
#     
#             deseriaziedArbXmlRequest = deserializedObject.toxml(encoding=constants.xml_encoding, element_name='ARBCreateSubscriptionResponse') 
#             deseriaziedArbXmlRequest = deseriaziedArbXmlRequest.replace(constants.nsNamespace1, '')
#             deseriaziedArbXmlRequest = deseriaziedArbXmlRequest.replace(constants.nsNamespace2, '')
#             logging.debug( "Good Dom Request: %s " % deseriaziedArbXmlRequest )
#             print( "ARB Dom Request: %s \n" % deseriaziedArbXmlRequest )
#             print("de-serialized successfully. ARBCreateTransaction \n ")
#         except Exception as ex:
#             print("failed to de-serialized successfully. ARBCreateTransaction \n ")
#             logging.error( 'Create Document Exception: %s, %s', type(ex), ex.args )  
#             
#             
# if __name__ =='__main__':
#     unittest.main()  
