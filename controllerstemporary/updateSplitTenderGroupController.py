             
class updateSplitTenderGroupController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(updateSplitTenderGroupController, self).__init__(apirequest, requestType)
        return 
    
    def validateRequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xxx == "null"):
        #    raise ValueError('xxx is required')         
        return

    def getResponseClass(self):
        ''' Returns the response class '''
        return apicontractsv1.updateSplitTenderGroupResponse()    