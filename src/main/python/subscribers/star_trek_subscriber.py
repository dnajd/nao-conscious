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
        self.vocab = ['data', 'phasers', 'tractor', 'hailing', 'torpedo', 'shields']

    def test_word(self, dict, key, word):

        t = 0.44 # confidence
        if key == word and dict[key] > t:
            return True
        return False

    def callback(self, eventName, value, subscriberIdentifier):

        self.nao.log('class=StarTrekSubscriber|method=callback|value=' + str(value))

        # get key with most confident match
        d = value
        key = max(d, key=d.get)
        
        # test words
        if self.test_word(d, key, 'data'):
            self.nao.say('i am commander data')

        elif self.test_word(d, key, 'phasers'):
            self.nao.say('fire when ready')

        elif self.test_word(d, key, 'tractor'):
            self.nao.say('engage and pull them in')

        elif self.test_word(d, key, 'hailing'):
            self.nao.say('bring up visuals')

        elif self.test_word(d, key, 'torpedo'):
            self.nao.say('shields up')

        elif self.test_word(d, key, 'shields'):
            self.nao.say('holding at 20 percent')

    def setup(self):
        self.nao.log('class=StarTrekSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=StarTrekSubscriber|method=teardown')

