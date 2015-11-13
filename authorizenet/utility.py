'''
Created on Nov 4, 2015

@author: krgupta
'''

from ConfigParser import SafeConfigParser
from ConfigParser import NoSectionError
'''import ConfigParser'''
import os
'''import logging'''
#from authorizenet.constants import constants

class helper(): 
    __parser = "null"
    __propertyfilename = "null"

    __initialized = False
    
    @staticmethod
    def getparser():
        return helper.__parser
    
    @staticmethod
    def getpropertyfile():
        return helper.__propertyfilename

    @staticmethod
    def setpropertyfile(propertyfilename):
        if (propertyfilename == 'null' or os.path.isfile(propertyfilename) == False):
            helper.__propertyfilename = 'null' 
        else:     
            helper.__propertyfilename = propertyfilename
        return

    @staticmethod
    def __classinitialized():
        return helper.__initialized
    
    @staticmethod
    def getproperty(propertyname):
        stringvalue = "null"
        temp = propertyname
        if ('null' != helper.getpropertyfile()):
                helper.__parser = SafeConfigParser({"http":"","https":"","ftp":""})
                if ('null' != helper.getparser()):
                    try:
                        if ( False == helper.__classinitialized()):
                            helper.getparser().read(helper.__propertyfilename)
                            __initialized = True
                    except:
                        print ("helper class not initialized")
                if (__initialized == True):
                    print (" Reading %s from property file %s" % (propertyname, helper.__propertyfilename))
                    stringvalue = helper.getparser().get("properties", propertyname)
                
        if ( "null" == stringvalue):
            stringvalue = os.getenv(temp)               
        return stringvalue 