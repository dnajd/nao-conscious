'''
Created on 1 April 2014
@author: don Najd
@description: Nao will be Sociable
'''
from __future__ import print_function

from naoutil import broker
import naoutil.naoenv as naoenv
import naoutil.memory as memory
from fluentnao.nao import Nao

from subscribers.laugh_subscriber import LaughSubscriber
from providers.tactile_touched_provider import TactileTouchedProvider

#########################
# SETUP
######################### 

# Broker (must come first)
#naoIp = "nao.local"
naoIp = "192.168.2.16"
broker.Broker('bootstrapBroker', naoIp=naoIp, naoPort=9559)

# FluentNao
env = naoenv.make_environment(None)
log = lambda msg: print(msg) 				# lambda for loggin to the console
nao = Nao(env, log)

# subscribers
laugh_subscriber = LaughSubscriber(nao)

# providers
tactile_provider = TactileTouchedProvider(nao, memory)


def shutdown():
	tactile_provider.teardown()	

def setup():
	tactile_provider.add_subscriber(laugh_subscriber)
	tactile_provider.setup()

setup()