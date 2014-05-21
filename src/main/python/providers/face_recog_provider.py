'''
Created on 20 May 2014

@author: Don Najd
@description: Provider for Naoqi Face Recognition
'''

class FaceRecogProvider(object):

    def __init__(self, nao, memory):

        # args
        self.nao = nao 
        self.memory = memory

        # provider properties
        self.running = False
        self.subscribers = []

        # facetracker
        self.nao.env.add_proxy("ALFaceTracker")   
        self.facetracker = self.nao.env.proxies["ALFaceTracker"] 

        # log
        self.nao.log('class=FaceRecogProvider|method=__init__')   

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        self.nao.log('class=FaceRecogProvider|method=add_subscriber')  

    def setup(self):
        self.memory.subscribeToEvent('FaceDetected', self.event_callback)
        self.nao.log('class=FaceRecogProvider|method=setup')  

        # face track
        self.nao.env.motion.setStiffnesses("Head", 1.0)
        #self.facetracker.startTracker()    

    def tear_down(self):
        self.memory.unsubscribeToEvent('FaceDetected')
        self.nao.log('class=FaceRecogProvider|method=teardown')  

        # face track
        self.nao.env.motion.setStiffnesses("Head", 0)
        #self.facetracker.stopTracker()   

    def event_callback(self, dataName, value, message): 
      
        # status
        self.running = True
        self.nao.log('class=FaceRecogProvider|method=event_callback|action=call_subscribers')  
        
        # call subscribers
        for s in self.subscribers:
            s.callback(dataName, value, message)

        self.running = False 
