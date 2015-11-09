# Authorize.Net Python SDK 

[![Build Status](https://travis-ci.org/AuthorizeNet/sdk-python.png?branch=master)]
(https://travis-ci.org/AuthorizeNet/sdk-python)

`pip install AuthorizeNet`

*** The Python SDK is still in limited Beta testing, please contact developer@authorize.net for more information ***

## Prerequisites

Requires 


## Installation
To install AuthorizeNet

`pip install AuthorizeNet`


## Registration & Configuration

Get a sandbox account at https://developer.authorize.net/sandbox  
Set your API credentials:  

````python
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'
````

For reporting tests, go to https://sandbox.authorize.net/ under Account tab->Transaction Details API and enable it.


## Usage
See our sample code repository at https://github.com/AuthorizeNet/sample-code-python

For the simplest "Hello World" example, use paste this into a file called charge-credit-card.py and run:

````python

````

## Building and Testing Source Code

Requirements
--------------------------------------
- python 2.7
- pyxb 1.2.4


Run the following to get pyxb and nosetests:
- pip install pyxb
- pip install nosetests
- pip install Magicmock

Testing
--------------------------------------
- Tests available are: unit tests, mock tests, sample code
- use nosetests to run all unittests 


