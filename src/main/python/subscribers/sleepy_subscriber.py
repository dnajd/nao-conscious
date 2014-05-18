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


    def callback(self, eventName, value, subscriberIdentifier):

        # happens every second, so no logging unless we need it
        #self.nao.log('class=SleepySubscriber|method=callback')

        if eventName == 'time_tracker':

            # time elapsed in sec
            start_datetime = value['start_datetime']
            elapsed_sec = round(float(value['elapsed_sec']))

            # I am sleepy
            if elapsed_sec == 5.0:
                self.nao.say('only five seconds and I am already sleepy')

            # log
            #self.nao.log('class=SleepySubscriber|method=callback|start_datetime={0}|elapsed_sec={1}'.format(start_datetime, str(elapsed_sec)))


    def setup(self):
        self.nao.log('class=SleepySubscriber|method=setup')
            

    def tear_down(self):
        self.nao.log('class=SleepySubscriber|method=teardown')
        