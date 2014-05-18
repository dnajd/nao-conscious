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

        self.sleepy_time = 1.0


    def callback(self, eventName, value, subscriberIdentifier):

        # happens every second, so no logging unless we need it
        #self.nao.log('class=SleepySubscriber|method=callback')

        if eventName == 'time_tracker':

            # time elapsed in sec
            #start_datetime = value['start_datetime']
            elapsed_min = round(float(value['elapsed_min']))

            
            if elapsed_min == self.sleepy_time:

                # I am sleepy
                self.nao.say('only {0} minutes awake and I am already sleepy'.format(self.sleepy_time))

                # increment sleepy time
                self.sleepy_time += random.randint(10, 60)

                # log
                self.nao.log('class=SleepySubscriber|method=callback|next_sleepy_time={0}'.format(self.sleepy_time))


    def setup(self):
        self.nao.log('class=SleepySubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=SleepySubscriber|method=teardown')
        