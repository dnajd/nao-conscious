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
# Broker

naoIp = "192.168.2.12" #"nao.local"
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
star_trek_subscriber = StarTrekSubscriber(nao)
voice_movement_subscriber = VoiceMovementSubscriber(nao)
#sensitive_subscriber = SensitiveSubscriber(nao)

# providers
time_provider = TimeProvider(nao)
touch_provider = TouchProvider(nao, memory, 'FrontTactilTouched')
face_recog_provider = FaceRecogProvider(nao, memory)
voice_recog_provider = VoiceRecogProvider(nao, memory)
#voice_emotion_provider = VoiceEmotionProvider(nao, memory)
# RightBumperPressed, LeftBumperPressed, ChestButtonPressed, FrontTactilTouched
# MiddleTactilTouched, RearTactilTouched, HandRightBackTouched, HandRightLeftTouched



#########################
# HELPERS


# shutdown with rear tactil
def tear_down(dataName, value, message):

	if value==1:
		nao.sit_say('Rest_1', 'Deactivate')

		# teardown
		touch_provider.tear_down()	
		time_provider.tear_down()
		face_recog_provider.tear_down()
		voice_recog_provider.tear_down()
	
memory.subscribeToEvent('RearTactilTouched', tear_down)

# setup all providers
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

	# voice emotion
	#voice_emotion_provider.add_subscriber(sensitive_subscriber)
	#voice_emotion_provider.setup()

# trigger setup
setup()



# learn face helper
def learn_face(name):
	# facetracker
	nao.env.add_proxy("ALFaceDetection")   
	face_detect = nao.env.proxies["ALFaceDetection"] 
	face_detect.learnFace(name)