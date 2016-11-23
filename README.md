# Authorize.Net Python SDK 

[![Travis](https://img.shields.io/travis/AuthorizeNet/sdk-python/master.svg)](https://travis-ci.org/AuthorizeNet/sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/AuthorizeNet/sdk-python/badge.svg?branch=master)](https://coveralls.io/github/AuthorizeNet/sdk-python?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/AuthorizeNet/sdk-python/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/AuthorizeNet/sdk-python/?branch=master)
[![PyPI](https://img.shields.io/pypi/v/authorizenet.svg)](https://badge.fury.io/py/authorizenet)

`pip install authorizenet`


## Prerequisites

We'll be ensuring this SDK is compatible with Python 2.6+, 3.2+ and PyPy but we're primarily testing against Python 2.7 so that's the current prerequisite.


## Installation
To install AuthorizeNet

`pip install authorizenet`


## Registration & Configuration

Get a sandbox account at https://developer.authorize.net/sandbox  
Set your API credentials:  

````python
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = 'YOUR_API_LOGIN_ID'
	merchantAuth.transactionKey = 'YOUR_TRANSACTION_KEY'
````


## Usage
See our sample code repository at https://github.com/AuthorizeNet/sample-code-python 

For the simplest "Hello World" example, paste this into a file called charge-credit-card.py and run:

````python
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = 'YOUR_LOGIN_ID'
merchantAuth.transactionKey = 'YOUR_TRANSACTION_KEY'

creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber = "4111111111111111"
creditCard.expirationDate = "2020-12"

payment = apicontractsv1.paymentType()
payment.creditCard = creditCard

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = "authCaptureTransaction"
transactionrequest.amount = Decimal ('1.55')
transactionrequest.payment = payment


createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId = "MerchantID-0001"

createtransactionrequest.transactionRequest = transactionrequest
createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()

response = createtransactioncontroller.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Transaction ID : %s" % response.transactionResponse.transId
else:
	print "response code: %s" % response.messages.resultCode

````
### Setting Production or Sandbox Environments  
To set the environment use the setenvironment method on the controller before executing.  E.g. for the example above:
````python
# Defaults to constants.SANDBOX for sandbox testing
createtransactioncontroller.setenvironment(constants.PRODUCTION)
````

## Building and Testing Source Code

Requirements
--------------------------------------
- python 2.7
- pyxb 1.2.4


Run the following to get pyxb and nosetests:
- pip install pyxb
- pip install unittest2
- pip install nose
- pip install lxml

Testing
--------------------------------------
- Tests available are: unit tests, mock tests, sample code
- use nosetests to run all unittests 
`
>nosetests
`

