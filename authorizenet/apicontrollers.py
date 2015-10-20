'''
Created on Oct18, 2015

@author: krgupta
'''
import logging
from authorizenet.constants import constants
from authorizenet import apicontractsv1
from authorizenet import apicontrollersbase             
class ARBCancelSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBCancelSubscriptionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBCancelSubscriptionResponse()                 
class ARBCreateSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBCreateSubscriptionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBCreateSubscriptionResponse()                 
class ARBGetSubscriptionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBGetSubscriptionListController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBGetSubscriptionListResponse()                 
class ARBGetSubscriptionStatusController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBGetSubscriptionStatusController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBGetSubscriptionStatusResponse()                 
class ARBUpdateSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBUpdateSubscriptionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBUpdateSubscriptionResponse()                 
class authenticateTestController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(authenticateTestController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.authenticateTestResponse()                 
class createCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createCustomerPaymentProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerPaymentProfileResponse()                 
class createCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createCustomerProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileResponse()                 
class createCustomerProfileFromTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createCustomerProfileFromTransactionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileResponse()                 
class createCustomerProfileTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createCustomerProfileTransactionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileTransactionResponse()                 
class createCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createCustomerShippingAddressController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerShippingAddressResponse()                 
class createTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(createTransactionController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.createTransactionResponse()                 
class decryptPaymentDataController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(decryptPaymentDataController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.decryptPaymentDataResponse()                 
class deleteCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(deleteCustomerPaymentProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerPaymentProfileResponse()                 
class deleteCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(deleteCustomerProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerProfileResponse()                 
class deleteCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(deleteCustomerShippingAddressController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerShippingAddressResponse()                 
class ErrorController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ErrorController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.ErrorResponse()                 
class getBatchStatisticsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getBatchStatisticsController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getBatchStatisticsResponse()                 
class getCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getCustomerPaymentProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerPaymentProfileResponse()                 
class getCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getCustomerProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerProfileResponse()                 
class getCustomerProfileIdsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getCustomerProfileIdsController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerProfileIdsResponse()                 
class getCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getCustomerShippingAddressController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerShippingAddressResponse()                 
class getHostedProfilePageController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getHostedProfilePageController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getHostedProfilePageResponse()                 
class getSettledBatchListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getSettledBatchListController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getSettledBatchListResponse()                 
class getTransactionDetailsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getTransactionDetailsController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        if (self._request.transId == "null"):              
            raise ValueError('transId is required')
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getTransactionDetailsResponse()                 
class getTransactionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getTransactionListController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getTransactionListResponse()                 
class getUnsettledTransactionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(getUnsettledTransactionListController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.getUnsettledTransactionListResponse()                 
class isAliveController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(isAliveController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.isAliveResponse()                 
class logoutController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(logoutController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.logoutResponse()                 
class mobileDeviceLoginController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(mobileDeviceLoginController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.mobileDeviceLoginResponse()                 
class mobileDeviceRegistrationController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(mobileDeviceRegistrationController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.mobileDeviceRegistrationResponse()                 
class sendCustomerTransactionReceiptController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(sendCustomerTransactionReceiptController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.sendCustomerTransactionReceiptResponse()                 
class updateCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(updateCustomerPaymentProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerPaymentProfileResponse()                 
class updateCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(updateCustomerProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerProfileResponse()                 
class updateCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(updateCustomerShippingAddressController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerShippingAddressResponse()                 
class updateSplitTenderGroupController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(updateSplitTenderGroupController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateSplitTenderGroupResponse()                 
class validateCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(validateCustomerPaymentProfileController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.validateCustomerPaymentProfileResponse()    