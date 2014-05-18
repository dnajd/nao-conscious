'''
Created on 11 May 2014

@author: Don Najd
@description: Nao will simply laugh
'''
import random

class LaughSubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=LaughSubscriber|method=__init__')   


    def callback(self, eventName, value, subscriberIdentifier):

        self.nao.log('class=LaughSubscriber|method=callback')

        # laugh
        self.nao.say('ha ha')
        self.nao.wait(2)


    def setup(self):
        self.nao.log('class=LaughSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=LaughSubscriber|method=teardown')
        