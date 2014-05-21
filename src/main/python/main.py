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

# providers
from providers.touch_provider import TouchProvider
from providers.time_provider import TimeProvider



#########################
# Broker

naoIp = "192.168.2.16" #"nao.local"
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

# providers
time_provider = TimeProvider(nao)
touch_provider = TouchProvider(nao, memory, 'FrontTactilTouched')

# Touch Provider Events:
# RightBumperPressed, LeftBumperPressed, ChestButtonPressed, FrontTactilTouched
# MiddleTactilTouched, RearTactilTouched, HandRightBackTouched, HandRightLeftTouched


#########################
# main.py

def teardown():

	# teardown
	touch_provider.tear_down()	
	time_provider.tear_down()

def setup():
	
	# time: sleepy & look around
	time_provider.add_subscriber(sleepy_subscriber)
	time_provider.add_subscriber(look_around_subscriber)
	time_provider.setup()

	# tactile: laugh
	touch_provider.add_subscriber(laugh_subscriber)
	touch_provider.setup()

setup()