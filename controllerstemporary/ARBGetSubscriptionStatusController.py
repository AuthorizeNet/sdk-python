               
class ARBGetSubscriptionStatusController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(ARBGetSubscriptionStatusController, self).__init__(apirequest, requestType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..')
        
        if (self._request.transId == "null"):
            raise ValueError('transId is required')           
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.ARBGetSubscriptionStatusResponse()    
        