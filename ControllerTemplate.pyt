             
class APICONTROLLERNAMEController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest, requestType):
        super(APICONTROLLERNAMEController, self).__init__(apirequest, requestType)
        return 
    
    def validaterequest(self):
        logging.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.APICONTROLLERNAMEResponse()    