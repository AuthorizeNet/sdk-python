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

Testing
--------------------------------------
- Tests available are: unit tests, mock tests, sample code
- use nosetests to run all unittests 

How to Use
--------------------------------------
The following is a sample which shows how to create a transaction request 
and execute it using the create transaction controller.

''''
from contract import binding
from decimal import *
from controller.CreateTransactionController import CreateTransactionController

class paymentTransaction(object):

	api_login_id = "your api login id"
	transaction_key = "your transaction key"
	ref_id = "your ref id"

	merchantAuthenticationOne = binding.merchantAuthenticationOne
	merchantAuthenticationOne.name = api_login_id
	merchantAuthenticationOne.transactionKey = transaction_key

	creditCardOne = binding.creditCardType()
	creditCardOne.cardNumber = "4111111111111111"
	creditCardOne.expirationDate = "2020-12"
	creditCardOne.cardCode = "999"
	paymentOne = binding.paymentType()
	paymentOne.creditCard = creditCardOne

	orderOne = binding.orderType()
	orderOne.invoiceNumber = "your invoice number"
	orderOne.description = "product description"

	customerOne = binding.customerDataType()
	customerOne.id = "numeric customerOne id"

	billToOne = binding.customerAddressType()
	billToOne.firstName = "first name"
	billToOne.lastName = "last name"
	billToOne.company = "company name"
	billToOne.address = "1 Main St"
	billToOne.city = "city name"
	billToOne.state = "state name"
	billToOne.zip = "numeric zipcode"
	billToOne.country = "country name"

	transactionRequestOne = binding.transactionRequestType()
	transactionRequestOne.transactionType = "authCaptureTransaction"
	transactionRequestOne.amount = Decimal("6.25")
	transactionRequestOne.paymentOne = paymentOne
	transactionRequestOne.orderOne = orderOne
	transactionRequestOne.customerOne = customerOne
	transactionRequestOne.billToOne = billToOne

	createTransactionRequest = binding.createTransactionRequest()
	createTransactionRequest.merchantAuthenticationOne = merchantAuthenticationOne
	createTransactionRequest.refId = ref_id
	createTransactionRequest.transactionRequestOne = transactionRequestOne

	createTransactionController = CreateTransactionController()
	createRequest = CreateTransactionController.CreateTransactionController(createTransactionRequest)
	CreateTransactionController.execute(createRequest, CreateTransactionController.getResponseClass())

	response = CreateTransactionController.getResponseObject()

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
''''

