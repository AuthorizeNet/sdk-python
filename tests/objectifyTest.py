from lxml import objectify

def objectifytest():
    xmlARB = '<?xml version="1.0" encoding="utf-8"?><ARBCreateSubscriptionResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd"><refId>Sample</refId><messages><resultCode>Ok</resultCode><message><code>I00001</code><text>Successful.</text></message></messages><subscriptionId>3998518</subscriptionId><profile><customerProfileId>40761707</customerProfileId><customerPaymentProfileId>37035233</customerPaymentProfileId></profile></ARBCreateSubscriptionResponse>'
    myobject = objectify.fromstring(xmlARB)
    print ("myobject.refId = %s \n" %myobject.refId)
    print ("myobject.subscriptionId = %s \n"%myobject.subscriptionId) 
    print ("myobject.messages.message.text = %s \n" %myobject.messages.message.text )
    
    xml1 ='<?xml version="1.0" encoding="utf-8"?><getTransactionDetailsResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd"><messages><resultCode>Ok</resultCode><message><code>I00001</code><text>Successful.</text></message></messages><transaction><transId>20000152262</transId><submitTimeUTC>2016-05-11T04:27:23.59Z</submitTimeUTC><submitTimeLocal>2016-05-10T21:27:23.59</submitTimeLocal><transactionType>authCaptureTransaction</transactionType><transactionStatus>settledSuccessfully</transactionStatus><responseCode>1</responseCode><responseReasonCode>1</responseReasonCode><responseReasonDescription>Approval</responseReasonDescription><authCode>ADJEM7</authCode><AVSResponse>Y</AVSResponse><cardCodeResponse>P</cardCodeResponse><batch><batchId>6030701</batchId><settlementTimeUTC>2016-05-12T02:34:34.223Z</settlementTimeUTC><settlementTimeLocal>2016-05-11T19:34:34.223</settlementTimeLocal><settlementState>settledSuccessfully</settlementState></batch><order><invoiceNumber>INV-12345</invoiceNumber><description>Product Description</description><purchaseOrderNumber>456654</purchaseOrderNumber></order><authAmount>5.00</authAmount><settleAmount>5.00</settleAmount><tax><amount>4.26</amount><description>level2 tax</description></tax><shipping><amount>4.26</amount><description>level2 tax</description></shipping><duty><amount>8.55</amount><description>duty description</description></duty><lineItems><lineItem><itemId>1</itemId><name>vase</name><description>Cannes logo</description><quantity>18.00000</quantity><unitPrice>45.00</unitPrice><taxable>false</taxable></lineItem></lineItems><taxExempt>false</taxExempt><payment><creditCard><cardNumber>XXXX0015</cardNumber><expirationDate>XXXX</expirationDate><cardType>MasterCard</cardType></creditCard></payment><customer><id>99999456654</id></customer><billTo><firstName>Ellen</firstName><lastName>Johnson</lastName><company>Souveniropolis</company><address>14 Main Street</address><city>Pecan Springs</city><state>TX</state><zip>44628</zip><country>USA</country></billTo><shipTo><firstName>China</firstName><lastName>Bayles</lastName><company>Thyme for Tea</company><address>12 Main Street</address><city>Pecan Springs</city><state>TX</state><zip>44628</zip><country>USA</country></shipTo><recurringBilling>false</recurringBilling><customerIP>192.168.1.1</customerIP><product>Card Not Present</product><entryMethod>Keyed</entryMethod><marketType>eCommerce</marketType></transaction></getTransactionDetailsResponse>'
    myobject = objectify.fromstring(xml1)

    itemDir = myobject.__dict__
    for i in itemDir:
        print ("myobject \n")
        print '{0}  :  {1}'.format(i, itemDir[i])
        print ("===================================================== \n")
        
        
        print ("myobject.messages.resultCode = %s \n" %myobject.messages.resultCode)
        print ("myobject.messages.message.code = %s \n" %myobject.messages.message.code)
        print ("myobject.messages.message.text = %s \n" %myobject.messages.message.text )
        print ("myobject.transactionResponse.resultCode = %s \n" %myobject.messages.resultCode)
        print ("myobject.transaction.transId = %s \n" %myobject.transaction.transId )
        print ("myobject.transaction.submitTimeUTC = %s \n" %myobject.transaction.submitTimeUTC )
#         print ("myobject.transaction.FDSFilterAction.FDSFilters.name = %s \n" %myobject.transaction.FDSFilterAction.FDSFilters.name)
        print ("myobject.transaction.batch.batchId = %s \n" %myobject.transaction.batch.batchId)
        print ("myobject.transaction.order.invoiceNumber = %s \n" %myobject.transaction.order.invoiceNumber)
#         print ("myobject.messages.resultCode = %s \n" %myobject.refId)
#         print ("myobject.messages.resultCode = %s \n" %myobject.refId)
#         print ("myobject.messages.resultCode = %s \n" %myobject.refId)
#         print ("myobject.messages.resultCode = %s \n" %myobject.refId)
#         print ("myobject.messages.resultCode = %s \n" %myobject.refId)
        
if __name__ =='__main__':
    i = 0
    for i in range(1):
        print( "i: %s \n" %i )
        objectifytest()
        i += 1