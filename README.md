# Authorize.Net Python SDK 

[![Travis](https://img.shields.io/travis/AuthorizeNet/sdk-python/master.svg)](https://travis-ci.org/AuthorizeNet/sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/AuthorizeNet/sdk-python/badge.svg?branch=master)](https://coveralls.io/github/AuthorizeNet/sdk-python?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/AuthorizeNet/sdk-python/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/AuthorizeNet/sdk-python/?branch=master)
[![PyPI](https://img.shields.io/pypi/v/authorizenet.svg)](https://badge.fury.io/py/authorizenet)


## Requirements

* Python 2.7 or greater
* OpenSSL 1.0.2 or greater
* An Authorize.Net account (see Registration & Configuration section below)


We'll be ensuring this SDK is compatible with Python 2.7+, 3.2+ and PyPy but we're primarily testing against Python 2.7.


## Installation

To install the AuthorizeNet Python SDK:

`pip install authorizenet`


## Registration & Configuration

Use of this SDK and the Authorize.Net APIs requires having an account on our system
Get a sandbox account at https://developer.authorize.net/sandbox  


### Authentication

Set your API credentials:  

```python
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = 'YOUR_API_LOGIN_ID'
	merchantAuth.transactionKey = 'YOUR_TRANSACTION_KEY'
```


### Setting Production or Sandbox Environments  
To set the environment use the setenvironment method on the controller before executing.  E.g. for the example above:
```python
# Defaults to constants.SANDBOX for sandbox testing
createtransactioncontroller.setenvironment(constants.PRODUCTION)
```

## Usage
See our sample code repository at https://github.com/AuthorizeNet/sample-code-python 

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

`>nosetests`


## License

This repository is destributed under a proprietary license. See the provided license file(../blob/master/LICENSE.txt).
This repository is destributed under a proprietary license. See the provided license file [../blob/master/LICENSE.txt] file.
This repository is destributed under a proprietary license. See the provided license file (../blob/master/LICENSE.txt) file.