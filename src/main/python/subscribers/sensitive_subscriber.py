'''
Created on 23 July 2014

@author: Don Najd
@description: Nao will be sensitive to stimulas
'''
import random
from datetime import datetime, timedelta

class SensitiveSubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=SensitiveSubscriber|method=__init__')

    def callback(self, eventName, value, subscriberIdentifier):

        self.nao.log('class=SensitiveSubscriber|method=callback|value=' + str(value))


    def setup(self):
        self.nao.log('class=SensitiveSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=SensitiveSubscriber|method=teardown')

