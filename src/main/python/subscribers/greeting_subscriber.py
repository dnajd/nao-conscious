'''
Created on 20 May 2014

@author: Don Najd
@description: Nao will greet you like a human
'''
import random
from datetime import datetime, timedelta

class GreetingSubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=GreetSubscriber|method=__init__')

        # subscriber properties  
        self.greetings = ['Greetings', 'Hello','Hello there','Hey','Hi','Hi there','How are you','How are you doing','Howdy','Hows it going','Salutations','Whats up']

    def callback(self, eventName, value, subscriberIdentifier):
        
        # name?
        if 'name' in value:
            name = value['name']
            if len(name) > 0:
                self.nao.log('class=GreetSubscriber|method=callback|name=' + name)

                # person
                if 'person' in value:
                    person = value['person']

                    # greet
                    if person.recognize_count==1 or person.recog_more_than_mins(5):
                        person.count_this_greeting()
                        self.nao.say(self.rand_greeting() + ' ' + person.name)


    def setup(self):
        self.nao.log('class=GreetSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=GreetSubscriber|method=teardown')


    # greeting
    def rand_greeting(self):
        
        i = random.randint(0,len(self.greetings))
        return self.greetings[i]


