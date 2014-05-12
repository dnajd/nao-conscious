'''
Created on 11 May 2014

@author: Don Najd
@description: Provider for tracking time
'''

import thread
import time

class TimeProvider(object):

    def __init__(self, nao):

        # args
        self.nao = nao 

        # provider properties
        self.running = False
        self.subscribers = []

        # log
        self.nao.log('class=TimeProvider|method=__init__')   

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        self.nao.log('class=TimeProvider|method=add_subscriber')  

    def setup(self):

        # start thread
        self.running = True
        args = self,
        thread.start_new_thread(self.time_tracker, args)

        # log
        self.nao.log('class=TimeProvider|method=setup')  

    def tear_down(self):
        # stop thread
        self.running = False
        self.nao.log('class=TimeProvider|method=teardown')  


    def time_tracker(self, time_provider): 

        while time_provider.running: 

            # wait 5 seconds
            time.sleep(5) 

            # run subscribers
            for s in self.subscribers:
                s.callback('', '', '')
