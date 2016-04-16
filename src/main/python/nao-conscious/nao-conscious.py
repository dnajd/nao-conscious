'''
Created on 1 April 2014
@author: Don Najd
@description: Nao will be Sociable
'''
# python
from __future__ import print_function

# SIGINT
import signal
import sys

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
from subscribers.star_trek_subscriber import StarTrekSubscriber
from subscribers.voice_movement_subscriber import VoiceMovementSubscriber
from subscribers.sensitive_subscriber import SensitiveSubscriber

# providers
from providers.touch_provider import TouchProvider
from providers.time_provider import TimeProvider
from providers.face_recog_provider import FaceRecogProvider
from providers.voice_recog_provider import VoiceRecogProvider
from providers.voice_emotion_provider import VoiceEmotionProvider


#########################
# SETUP: Broker

naoIp = "nao.local"
broker.Broker('bootstrapBroker', naoIp=naoIp, naoPort=9559)

#########################
# SETUP: FluentNao

env = naoenv.make_environment(None)
log = lambda msg: print(msg) 				# lambda for loggin to the console
nao = Nao(env, log)

# disable autonomous moves
nao.env.add_proxy("ALAutonomousMoves")
autonomous_moves = nao.env.proxies["ALAutonomousMoves"] 
autonomous_moves.setExpressiveListeningEnabled(False)


#########################
# SETUP: Nao Consious

# subscribers
laugh_subscriber = LaughSubscriber(nao)
sleepy_subscriber = SleepySubscriber(nao)
look_around_subscriber = LookAroundSubscriber(nao)
greeting_subscriber = GreetingSubscriber(nao)
star_trek_subscriber = StarTrekSubscriber(nao)
voice_movement_subscriber = VoiceMovementSubscriber(nao)

# providers
time_provider = TimeProvider(nao)
touch_provider = TouchProvider(nao, memory, 'FrontTactilTouched')
face_recog_provider = FaceRecogProvider(nao, memory)
voice_recog_provider = VoiceRecogProvider(nao, memory)

# sensors
# RightBumperPressed, LeftBumperPressed, ChestButtonPressed, FrontTactilTouched
# MiddleTactilTouched, RearTactilTouched, HandRightBackTouched, HandRightLeftTouched



#########################
# HELPER: tear down
def tear_down():
	nao.sit_say('Rest_1', 'Deactivate')

	# teardown
	touch_provider.tear_down()	
	time_provider.tear_down()
	face_recog_provider.tear_down()
	voice_recog_provider.tear_down()
	memory.unsubscribeToEvent('RearTactilTouched')  

# sigint
def tear_down_signal_handler(signal, frame):
    tear_down()
    sys.exit(0)

signal.signal(signal.SIGINT, tear_down_signal_handler)
	
# tactil
def tear_down_tactil_handler(dataName, value, message):
	if value==1:
		tear_down()

memory.subscribeToEvent('RearTactilTouched', tear_down_tactil_handler)



#########################
# HELPER: Example Nao Conscious
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

	# voice recog
	voice_recog_provider.add_subscriber(star_trek_subscriber)
	voice_recog_provider.add_subscriber(voice_movement_subscriber)
	voice_recog_provider.setup()

# trigger setup
setup()


####################
# EXPERIMENT: animiations
def salute():
	nao.set_duration(1.0)

	# up to forehead
	nao.arms.right_forward(0,21.0,6.0)
	nao.elbows.right_bent(0,-5.0).right_turn_up(0,-42.0)
	nao.wrists.right_center(0,15.0)
	nao.hands.right_close(0).go()

	# out
	nao.arms.right_forward(0,20.0,8.0)
	nao.elbows.right_straight(0,-43.0).right_turn_up(0,-38.0)
	nao.hands.right_open().go()

	# down to neutral
	nao.arms.right_down(0,41.0,3.0).elbows.turn_in(0,-27.0).right_bent(0,-41.0)
	nao.hands.right_close(0).go()

def wave():
	nao.set_duration(1.0)

	# up
	nao.arms.right_forward(0,5.0,4.0).elbows.right_bent(0,-18.0).right_turn_in(0,-17.0)
	nao.wrists.right_turn_out(0,-35.0).hands.right_close(0).go()

	# outward
	nao.arms.right_forward(0,-3.0,35.0).left_down(0,36.0,15.0).elbows.right_turn_up(0,12.0).left_turn_in(0,-30.0)
	nao.wrists.left_center(0,3.0).right_center(0,8.0).hands.right_open().go()

	# down
	nao.arms.right_down(0,41.0,23.0).elbows.right_bent(0,-15.0).right_turn_in(0,-14.0)
	nao.wrists.center(0,3.0).go()

def tada(statement):
	nao.set_duration(1.0)

	nao.hands.close()
	nao.leds.off()

	# ta da
	nao.hands.open(0)
	nao.head.forward(0,17.0).down(0,-19.0)
	nao.arms.right_up(0,-35.0,26.0).left_forward(0,-39.0,14.0)
	nao.elbows.right_straight(0,-22.0).right_turn_up(0,-12.0).left_bent(0,-45.0).left_turn_up(0,28.0)
	nao.wrists.left_turn_in(0,-23.0)
	nao.leds.eyes(0x7ac5cd).ears(0x7ac5cd).chest(0x7ac5cd).feet(0x7ac5cd)
	nao.say(statement)
	nao.go()

	# sit
	nao.head.forward(0,-1.0).center(0,-1.0)
	nao.arms.right_down(0,34.0,16.0).left_down(0,38.0,12.0).elbows.turn_in(0,-29.0).right_bent(0,-18.0).left_bent(0,-20.0)
	nao.wrists.center(0,3.0).hands.right_close(0).left_open(0).go()

#########################
# EXPERIMENT: Dialog
def load():

	# load topic
	topic = nao.dialog.loadTopic("/home/nao/topics/startrek.top")
	nao.dialog.activateTopic(topic)
	nao.dialog.subscribe(topic)
	#dialog.startPush()

	return topic

# unload
def unload():
	nao.dialog.deactivateTopic(topic)
	nao.dialog.unloadTopic(topic)
	nao.dialog.unsubscribe(topic)
	#undialog.stopPush()

# run
#topic = load()
