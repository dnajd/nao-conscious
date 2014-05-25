'''
Created on 17 May 2014

@author: Don Najd
@description: Nao will get sleepy after a while
'''
import random

class SleepySubscriber(object):

    def __init__(self, nao):

        self.nao = nao 
        self.nao.log('class=SleepySubscriber|method=__init__')   

        self.sleepy_time = 60.0


    def callback(self, eventName, value, subscriberIdentifier):

        # happens every second, so no logging unless we need it
        #self.nao.log('class=SleepySubscriber|method=callback')

        if eventName == 'time_tracker':

            # time elapsed in sec
            #start_datetime = value['start_datetime']
            elapsed_min = round(float(value['elapsed_min']))

            
            if elapsed_min == self.sleepy_time:

                # I am sleepy
                self.nao.say('we have been working for an hour. I would like to take a nap')

                # log
                self.nao.log('class=SleepySubscriber|method=callback')


    def setup(self):
        self.nao.log('class=SleepySubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=SleepySubscriber|method=teardown')
        