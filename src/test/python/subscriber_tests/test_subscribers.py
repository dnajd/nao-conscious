from __future__ import print_function

'''
Created on 19 May 2014
@author: Don Najd
@description: Unit test main
'''

import unittest
from mock import patch, Mock, MagicMock

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
from subscribers.sensitive_subscriber import SensitiveSubscriber

# providers
from providers.touch_provider import TouchProvider
from providers.time_provider import TimeProvider

class TestSubscribers(unittest.TestCase):

	def setUp(self):

		# setup env
		self.env = MagicMock()
		self.log = lambda msg: print(msg)
		self.nao = MagicMock()
		#self.nao.log = self.log

	def testEnvAndMocking(self):

		# mock nao.say
		self.nao.say.return_value = True

		# call say (normally happens internal to another class)
		result = self.nao.say('hi')

		# assert called with
		self.nao.say.assert_called_once_with('hi')

		# assert result
		self.assertEqual(True, result, "nao.say should return true")

	def testLaughSubscriber(self):

		# subscribers
		subscriber = LaughSubscriber(self.nao)
		subscriber.callback('', '', '')

		# assert callback executed say
		self.nao.say.assert_called_once_with('ha ha')

	def testSleepySubscriber(self):

		# mock value
		value = MagicMock()
		value['elapsed_min'] = '10.0'

		# event name
		eventName = 'time_tracker'

		subscriber = SleepySubscriber(self.nao)
		subscriber.callback(eventName, value, '')


	def testLookAroundSubscriber(self):

		# mock value
		value = MagicMock()
		value['elapsed_sec'] = '10.0'
		
		# event name
		eventName = 'time_tracker'

		subscriber = LookAroundSubscriber(self.nao)
		subscriber.callback(eventName, value, '')


	def testGreetingSubscriber(self):
		
		# mock value
		value = MagicMock()
		value[1][1][1][0] = 'don'

		# test subscriber
		subscriber = GreetingSubscriber(self.nao)
		subscriber.callback('', value, '')



	def testStarTrekSubscriber(self):
		
		# mock value
		value = MagicMock()
		value = dict({ 'phasers': 0.50, 'comander data': 0.10 })

		# test subscriber
		subscriber = StarTrekSubscriber(self.nao)
		subscriber.callback('', value, '')

	def testSensitiveSubscriber(self):

		# test subscriber
		subscriber = SensitiveSubscriber(self.nao)
		subscriber.callback('', '', '')


if __name__ == "__main__":
    unittest.main()

