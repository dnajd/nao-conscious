'''
Created on 5 June 2014

@author: Don Najd
@description: Nao will respond if star trek words are recognized
'''
import random
from datetime import datetime, timedelta

class StarTrekSubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=StarTrekSubscriber|method=__init__')
        self.vocab = ['comander data', 'phasers', 'tractor beam', 'hailing', 'torpedo', 'shields']


    def callback(self, eventName, value, subscriberIdentifier):

        self.nao.log('class=StarTrekSubscriber|method=callback|value=' + str(value))

        d = value
        t = 0.48

        key = 'comander data'
        if key in d and d[key] > t:
            self.nao.say('i am commander data')

        key = 'phasers'
        if key in d and d[key] > t:
            self.nao.say('fire when ready')

        key = 'tractor beam'
        if key in d and d[key] > t:
            self.nao.say('engage and pull them in')

        key = 'hailing'
        if key in d and d[key] > t:
            self.nao.say('bring up visuals')

        key = 'torpedo'
        if key in d and d[key] > t:
            self.nao.say('shields up')

        key = 'shields'
        if key in d and d[key] > t:
            self.nao.say('holding at 20 percent')

    def setup(self):
        self.nao.log('class=StarTrekSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=StarTrekSubscriber|method=teardown')

