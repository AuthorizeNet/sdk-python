'''
Created on Oct16, 2015

@author: krgupta
'''
import logging
from authorizenet.constants import constants
from authorizenet import apicontractsv1
from authorizenet import apicontrollersbase

              
        
class ARBCancelSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ARBCancelSubscriptionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBCancelSubscriptionResponse()

    
                
class ARBCreateSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ARBCreateSubscriptionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBCreateSubscriptionResponse()

    
                
class ARBGetSubscriptionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ARBGetSubscriptionListController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBGetSubscriptionListResponse()

    
                
class ARBGetSubscriptionStatusController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ARBGetSubscriptionStatusController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBGetSubscriptionStatusResponse()

    
                
class ARBUpdateSubscriptionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ARBUpdateSubscriptionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBUpdateSubscriptionResponse()

    
                
class authenticateTestController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(authenticateTestController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.authenticateTestResponse()

    
                
class createCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createCustomerPaymentProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerPaymentProfileResponse()

    
                
class createCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createCustomerProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileResponse()

    
                
class createCustomerProfileFromTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createCustomerProfileFromTransactionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileResponse()

    
                
class createCustomerProfileTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createCustomerProfileTransactionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerProfileTransactionResponse()

    
                
class createCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createCustomerShippingAddressController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createCustomerShippingAddressResponse()

    
                
class createTransactionController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(createTransactionController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.createTransactionResponse()

    
                
class decryptPaymentDataController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(decryptPaymentDataController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.decryptPaymentDataResponse()

    
                
class deleteCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(deleteCustomerPaymentProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerPaymentProfileResponse()

    
                
class deleteCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(deleteCustomerProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerProfileResponse()

    
                
class deleteCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(deleteCustomerShippingAddressController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerShippingAddressResponse()

    
                
class ErrorController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(ErrorController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ErrorResponse()

    
                
class getBatchStatisticsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getBatchStatisticsController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getBatchStatisticsResponse()

    
                
class getCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getCustomerPaymentProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerPaymentProfileResponse()

    
                
class getCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getCustomerProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerProfileResponse()

    
                
class getCustomerProfileIdsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getCustomerProfileIdsController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerProfileIdsResponse()

    
                
class getCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getCustomerShippingAddressController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getCustomerShippingAddressResponse()

    
                
class getHostedProfilePageController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getHostedProfilePageController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getHostedProfilePageResponse()

    
                
class getSettledBatchListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getSettledBatchListController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getSettledBatchListResponse()

    
                
class getTransactionDetailsController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getTransactionDetailsController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getTransactionDetailsResponse()

    
                
class getTransactionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getTransactionListController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getTransactionListResponse()

    
                
class getUnsettledTransactionListController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(getUnsettledTransactionListController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.getUnsettledTransactionListResponse()

    
                
class isAliveController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(isAliveController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.isAliveResponse()

    
                
class logoutController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(logoutController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.logoutResponse()

    
                
class mobileDeviceLoginController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(mobileDeviceLoginController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.mobileDeviceLoginResponse()

    
                
class mobileDeviceRegistrationController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(mobileDeviceRegistrationController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.mobileDeviceRegistrationResponse()

    
                
class sendCustomerTransactionReceiptController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(sendCustomerTransactionReceiptController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.sendCustomerTransactionReceiptResponse()

    
                
class updateCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(updateCustomerPaymentProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerPaymentProfileResponse()

    
                
class updateCustomerProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(updateCustomerProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerProfileResponse()

    
                
class updateCustomerShippingAddressController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(updateCustomerShippingAddressController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateCustomerShippingAddressResponse()

    
                
class updateSplitTenderGroupController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(updateSplitTenderGroupController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateSplitTenderGroupResponse()

    
                
class validateCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType, responseType):
        super(validateCustomerPaymentProfileController, self).__init__(apirequest, requestType, responseType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.validateCustomerPaymentProfileResponse()

    
        