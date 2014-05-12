'''
Created on 1 April 2014
@author: don Najd
@description: Nao will be Sociable
'''

# python
from __future__ import print_function

# fluent nao
from naoutil import broker
import naoutil.naoenv as naoenv
import naoutil.memory as memory
from fluentnao.nao import Nao

# nao consious
from subscribers.laugh_subscriber import LaughSubscriber
from providers.tactile_touched_provider import TactileTouchedProvider
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

laugh_subscriber = LaughSubscriber(nao)
time_provider = TimeProvider(nao)
tactile_provider = TactileTouchedProvider(nao, memory)


#########################
# main.py

def shutdown():
	tactile_provider.tear_down()	
	time_provider.tear_down()

def setup():
	
	time_provider.add_subscriber(laugh_subscriber)
	time_provider.setup()

	tactile_provider.add_subscriber(laugh_subscriber)
	tactile_provider.setup()

setup()