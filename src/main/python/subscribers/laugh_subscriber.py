'''
Created on 11 May 2014

@author: Don Najd
@description: Nao will simply laugh
'''
from datetime import datetime, timedelta
import random

class LaughSubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=LaughSubscriber|method=__init__')   


    # CALLBACKS
    def callback(self, dataName, value, message):
        self.nao.log('class=LaughSubscriber|method=callback')
        self.nao.say('ha ha')


    def setup(self):
        self.nao.log('class=LaughSubscriber|method=setup')
            

    def teardown(self):
        self.nao.log('class=LaughSubscriber|method=teardown')
        