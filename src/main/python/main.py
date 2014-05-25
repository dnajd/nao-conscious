'''
Created on 1 April 2014
@author: Don Najd
@description: Nao will be Sociable
'''

# python
from __future__ import print_function

# naoutil & fluentnao
from naoutil import broker
import naoutil.naoenv as naoenv
import naoutil.memory as memory
from fluentnao.nao import Nao

# subscribers
from subscribers.laugh_subscriber import LaughSubscriber
from subscribers.sleepy_subscriber import SleepySubscriber
from subscribers.look_around_subscriber import LookAroundSubscriber
from subscribers.greeting_subscriber import GreetingSubscriber

# providers
from providers.touch_provider import TouchProvider
from providers.time_provider import TimeProvider
from providers.face_recog_provider import FaceRecogProvider



#########################
# Broker

naoIp = "192.168.2.17" #"nao.local"
broker.Broker('bootstrapBroker', naoIp=naoIp, naoPort=9559)


#########################
# FluentNao

env = naoenv.make_environment(None)
log = lambda msg: print(msg) 				# lambda for loggin to the console
nao = Nao(env, log)


#########################
# Nao Consious

# subscribers
laugh_subscriber = LaughSubscriber(nao)
sleepy_subscriber = SleepySubscriber(nao)
look_around_subscriber = LookAroundSubscriber(nao)
greeting_subscriber = GreetingSubscriber(nao)

# providers
time_provider = TimeProvider(nao)
touch_provider = TouchProvider(nao, memory, 'FrontTactilTouched')
face_recog_provider = FaceRecogProvider(nao, memory)
# RightBumperPressed, LeftBumperPressed, ChestButtonPressed, FrontTactilTouched
# MiddleTactilTouched, RearTactilTouched, HandRightBackTouched, HandRightLeftTouched



#########################
# main.py

def tear_down():

	# teardown
	touch_provider.tear_down()	
	time_provider.tear_down()
	face_recog_provider.tear_down()

def setup():
	
	# time: sleepy & look around
	time_provider.add_subscriber(sleepy_subscriber)
	time_provider.add_subscriber(look_around_subscriber)
	time_provider.setup()

	# tactile: laugh
	touch_provider.add_subscriber(laugh_subscriber)
	touch_provider.setup()

	# face recog
	face_recog_provider.add_subscriber(greeting_subscriber)
	face_recog_provider.setup()

setup()


def learn_face(name):
	# facetracker
	nao.env.add_proxy("ALFaceDetection")   
	face_detect = nao.env.proxies["ALFaceDetection"] 
	face_detect.learnFace(name)
