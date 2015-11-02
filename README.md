# sdk-python    [![Build Status](https://magnum.travis-ci.com/egodolja/sdk-python.svg?token=9z5hnp59uHpbBpKa445s&branch=master)](https://magnum.travis-ci.com/egodolja/sdk-python)
Python SDK for the Authorize.Net API

Installations
--------------------------------------
- python 2.7
- Editor of your choice (I used PyDev for Eclipse)
- pyxb 1.2.4
 *install python before pyxb 

Run the following to get pyxb and nosetests:
- pip install pyxb
- pip install nosetests
- pip install Magicmock

Testing
--------------------------------------
- Tests available are: unit tests, mock tests, sample code
- use nosetests to run all unittests 

How to Use
--------------------------------------
You need to set your credentials.
Refer to template given in anet_python_sdk_properties.ini
Either copy it to your root directory or make a new one similar to this. If you create one name file anet_python_sdk_properties.ini

The following is a sample which shows how to create a transaction request 
and execute it using the create transaction controller.

from authorizenet import apicontractsv1
from decimal import *
from authorizenet.apicontrollers import CreateTransactionController

class paymentTransaction(object):
	
	#set sandbox credentials and refid
	api_login_id = "your api login id"
	transaction_key = "your transaction key"
	ref_id = "your ref id"
	
	#create merchant authentication using sandbox credentials
	merchantAuthenticationOne = binding.merchantAuthenticationOne
	merchantAuthenticationOne.name = api_login_id
	merchantAuthenticationOne.transactionKey = transaction_key

	#create credit card by filling out the following minimum requirements
	creditCardOne = binding.creditCardType()
	creditCardOne.cardNumber = "4111111111111111"
	creditCardOne.expirationDate = "2020-12"
	creditCardOne.cardCode = "999"
	paymentOne = binding.paymentType()
	paymentOne.creditCard = creditCardOne

	#create order with details
	orderOne = binding.orderType()
	orderOne.invoiceNumber = "your invoice number"
	orderOne.description = "product description"

	#create customer; the following are minimum requirements
	customerOne = binding.customerDataType()
	customerOne.id = "numeric customerOne id"

	#create billTo information
	billToOne = binding.customerAddressType()
	billToOne.firstName = "first name"
	billToOne.lastName = "last name"
	billToOne.company = "company name"
	billToOne.address = "1 Main St"
	billToOne.city = "city name"
	billToOne.state = "state name"
	billToOne.zip = "numeric zipcode"
	billToOne.country = "country name"

	#create transaction request 
	transactionRequestOne = binding.transactionRequestType()
	transactionRequestOne.transactionType = "authCaptureTransaction"
	transactionRequestOne.amount = Decimal("6.25")
	transactionRequestOne.paymentOne = paymentOne
	transactionRequestOne.orderOne = orderOne
	transactionRequestOne.customerOne = customerOne
	transactionRequestOne.billToOne = billToOne

	#build the createTransactionRequest 
	createTransactionRequest = binding.createTransactionRequest()
	createTransactionRequest.merchantAuthenticationOne = merchantAuthenticationOne
	createTransactionRequest.refId = ref_id
	createTransactionRequest.transactionRequestOne = transactionRequestOne

	#create the controller which is used to build xml and execute it
	createTransactionController = CreateTransactionController()
	createRequest = CreateTransactionController.CreateTransactionController(createTransactionRequest)
	CreateTransactionController.execute(createRequest, CreateTransactionController.getResponseClass())

	#get the object from the response
	response = CreateTransactionController.getResponseObject()

	#check the response for details
	if response:
		if response.messages.resultCode == 'OK':
			result = response.transactionResponse
			if result.responseCode == '1':
				print result.responseCode
				print 'Successful Credit Card Transaction'
				print ('authCode : %s' % result.authCode)
				print ('transId: %s' % result.transId)
			else:
				print ('Failed transaction %s' % result.responseCode)
		else:
			print ('Failed transaction %s' % response.messages.resultCode)

	print '---------------------------------------------'

