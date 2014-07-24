'''
Created on 23 July 2014

@author: Don Najd
@description: Provider for Naoqi Voice Emotion Analysis
'''
from time import sleep

class VoiceEmotionProvider(object):

    def __init__(self, nao, memory):

        # args
        self.nao = nao 
        self.memory = memory

        # proxy
        self.nao.env.add_proxy("ALVoiceEmotionAnalysis")
        self.voice_emotion_analysis = self.nao.env.proxies["ALVoiceEmotionAnalysis"] 

        # provider properties
        self.running = False
        self.subscribers = []

        # log
        self.nao.log('class=VoiceEmotionAnalysis|method=__init__')   

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        self.nao.log('class=VoiceEmotionAnalysis|method=add_subscriber')  

    def setup(self):

        # subscribe
        self.memory.subscribeToEvent('EmotionRecognized', self.event_callback)
        self.nao.log('class=VoiceEmotionAnalysis|method=setup')  

    def tear_down(self):
        
        # unsubscribe
        self.memory.unsubscribeToEvent('EmotionRecognized')
        self.nao.log('class=VoiceEmotionAnalysis|method=teardown')  

    def event_callback(self, naoqi_dataName, naoqi_value, naoqi_message): 

        if self.running == False:

            # status
            self.running = True
            self.nao.log('class=VoiceEmotionAnalysis|method=event_callback|action=call_subscribers')  

            # call subscribers
            for s in self.subscribers:
                s.callback(naoqi_dataName, naoqi_value, naoqi_message)

            self.nao.log('class=VoiceEmotionAnalysis|method=event_callback|action=call_subscribers_complete')  
            self.running = False 

            