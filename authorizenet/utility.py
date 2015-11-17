'''
Created on Nov 4, 2015

@author: krgupta
'''

from ConfigParser import SafeConfigParser
from ConfigParser import NoSectionError
import os
import sys
#from __future__ import print_function

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

        if ('null' != helper.getpropertyfile()):
            if (False == helper.__classinitialized()):
                if ('null' == helper.getparser()):
                    try:
                        helper.__parser = SafeConfigParser({"http":"","https":"","ftp":""})
                    except:
                        print ("Parser could not be initialized")

                if ('null' != helper.getparser()):
                    try:
                        helper.getparser().read(helper.__propertyfilename)
                        helper.__initialized = True
                    except:
                        print ("Unable to load the property file")

        if (True == helper.__classinitialized()):
            try:
                stringvalue = helper.getparser().get("properties", propertyname)
            except:
                sys.stderr.write("%s not found" %propertyname )
                
        if ( "null" == stringvalue):
            stringvalue = os.getenv(propertyname)               
        return stringvalue 