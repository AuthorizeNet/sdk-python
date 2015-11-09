'''
Created on Nov 4, 2015

@author: krgupta
'''

from ConfigParser import SafeConfigParser
'''import ConfigParser'''
import os
'''import logging'''
#from authorizenet.constants import constants

class helper(): 
    __parser = SafeConfigParser({"http":"","https":"","ftp":""})
    __propertyfilename = "null"

    __initialized = 'False'
    
    @staticmethod
    def getpropertyfile():
        return helper.__propertyfilename

    @staticmethod
    def getparser():
        return helper.__parser
    
    @staticmethod
    def setpropertyfile(propertyfilename):
        if (propertyfilename == 'null' or os.path.isfile(propertyfilename) == 'False'):
            raise ValueError('properties '%propertyfilename%' file not found') 
        
        helper.__propertyfilename = propertyfilename
        return

    @staticmethod
    def __classinitialized():
        return helper.__initialized
    
    @staticmethod
    def getproperty(propertyname):
        
        if ( 'False' == helper.__classinitialized()):
            helper.getparser().read(helper.__propertyfilename)
            __initialized = 'True'
        
        stringvalue = "null"
        if ("null" != helper.getparser()):
            stringvalue = helper.getparser().get("properties", propertyname)
        else :
            print (" property file does not exist, will read from environment")
            stringvalue = os.getenv[propertyname]                

        return stringvalue 
    
    @staticmethod
    def setproperty(propertyname):
        helper.getparser().add_option("properties", propertyname)
        return
