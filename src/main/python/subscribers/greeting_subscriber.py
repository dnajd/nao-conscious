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
        self.logged_recog = {}  
        self.greetings = ['Greetings', 'Hello','Hello there','Hey','Hi','Hi there','How are you','How are you doing','Howdy','Hows it going','Salutations','Whats up']

    def callback(self, eventName, value, subscriberIdentifier):
        try:
            name = value[1][1][1][0]    # get name from naoqi
        except IndexError:
            name = ''

        if len(name) > 0:
            
            # log
            self.nao.log('class=GreetSubscriber|method=callback|name=' + name)

            # new person?
            if not name in self.logged_recog:

                # create & log person
                person = Person(name)
                self.logged_recog[name] = person
                person.track_recognition()

                # greet
                self.play_greeting(person)
            else:
                person = self.logged_recog[name]
                person.track_recognition()

                 # greet?
                person = self.logged_recog[name]
                if person.recog_more_than_mins(5):
                    self.play_greeting(person)


    def setup(self):
        self.nao.log('class=GreetSubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=GreetSubscriber|method=teardown')


    # greeting
    def rand_greeting(self):
        
        i = random.randint(0,len(self.greetings))
        return self.greetings[i]

    def play_greeting(self, person):

        # track greeting
        person.track_greeting()

        # do greeting
        self.nao.say(self.rand_greeting() + ' ' + person.name)


# Tracking
class Person(object):

    def __init__(self, name):

        # args
        self.name = name
        self.recognize_count = 0
        self.recognize_track = []
        self.greet_count = 0
        self.greet_track = []
        
    def track_recognition(self):
        self.recognize_count += 1
        self.last_recognized = datetime.now()
        self.recognize_track.append(self.last_recognized)

    def track_greeting(self):
        self.greet_count += 1
        self.greet_track.append(datetime.now())

    def recog_more_than_mins(self, minutes):

        time_past = datetime.now() - self.last_recognized
        if time_past > timedelta(minutes=minutes):
            return True
        return False
