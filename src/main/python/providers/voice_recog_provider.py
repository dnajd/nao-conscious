'''
Created on 5 June 2014

@author: Don Najd
@description: Provider for Naoqi Voice Recog
'''

class VoiceRecogProvider(object):

    def __init__(self, nao, memory, vocab='hello'):

        # args
        self.nao = nao 
        self.memory = memory
        self.vocab = vocab

        # provider properties
        self.running = False
        self.subscribers = []

        # log
        self.nao.log('class=VoiceRecogProvider|method=__init__')   

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        self.nao.log('class=VoiceRecogProvider|method=add_subscriber')  

    def setup(self):
        # initial vocab
        nao.env.speechRecognition.setVocabulary(self.vocab, True)

        memory.subscribeToEvent('WordRecognized', self.event_callback)
        self.nao.log('class=VoiceRecogProvider|method=setup|vocab=' + self.vocab)  

    def tear_down(self):
        memory.unsubscribeToEvent('WordRecognized')
        self.nao.log('class=VoiceRecogProvider|method=teardown')  

    def event_callback(self, naoqi_dataName, naoqi_value, naoqi_message): 

        # zip into dictionary; {phrase: confidence}
        naoqi_value = dict(zip(value[0::2], value[1::2]))

        # status
        self.running = True
        self.nao.log('class=VoiceRecogProvider|method=event_callback|action=call_subscribers')  
        
        # call subscribers
        for s in self.subscribers:
            s.callback(naoqi_dataName, naoqi_value, naoqi_message)

        self.running = False 
