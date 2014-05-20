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

# providers
from providers.tactile_touched_provider import TactileTouchedProvider
from providers.time_provider import TimeProvider

class TestSubscribers(unittest.TestCase):

	def setUp(self):

		# setup env
		self.env = Mock()
		self.log = lambda msg: print(msg)
		self.nao = Mock()

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
		laugh_subscriber = LaughSubscriber(self.nao)
		laugh_subscriber.callback('','','')

		# assert callback executed say
		self.nao.say.assert_called_once_with('ha ha')

	def testSleepySubscriber(self):

		sleepy_subscriber = SleepySubscriber(self.nao)
		sleepy_subscriber.callback('','','')


	def testLookAroundSubscriber(self):
		
		look_around_subscriber = LookAroundSubscriber(self.nao)
		look_around_subscriber.callback('','','')


if __name__ == "__main__":
    unittest.main()
