'''
Created on Jun 8, 2015

@author: egodolja
'''
class constants(object):
    '''xml headers'''
    headers = {'Content-Type' : 'application/xml', 'version' : '1.0', 'encoding' : 'utf-8'}
    
    '''ARBGetSubscriptionStatus <Status> tag'''
    StatusStart = '<Status>'
    StatusEnd = '</Status>'
    
    '''xml encoding'''
    xml_encoding = 'utf-8'
    
    '''response encoding'''
    response_encoding = 'ISO-8859-1'
    
    '''note section of subscription status response'''
    note = ' note="Status with a capital \'S\' is obsolete."'
    
    '''ns namespace 1'''
    nsNamespace1 = 'ns1:'
    
    '''ns namespace 2'''
    nsNamespace2 = ':ns1'
