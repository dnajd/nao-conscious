# Summary

Make Nao come to life through events that trigger movement and speech.

# Goals

* Autonomy & Sociability
* Cute & Fun
* Like a Pet

# Project Name

* marionette

# Features

Wake up behavior
 * knows how long he's been asleep
 * has something to do / say about it

Eye contact with people
 * using the face tracker for the most basic social tactic

Face Recognition
 * log: who, when, last view (how long ago) & how many time
 * express familiarity through warm / cold greetings based on stats
 * even add predictability with stats; ex. someone should be here right now

Word Recognition
 * library of responses to build vocabulary
 * randomize to choose between competing possible responses

Movement
 * random movement to express vitality
 * triggered movement based on: time of day, face recognition, sound localization, word recognition, lighting in the room

Probability
 * give events a probability of happening or not
 * used to choose between multiple possible events / actions
 * used to create a sense of identity, preference, personality
 * try to not repeat itself too much through modifiers & logging

Touch
 * combo codes on touch sensors
 * inteligent reaction to touch

# Architecture & Notes

## Event Management Abstractions

Phase I. Start with providers calling subscribers directly. No thread safety.

Subscribers - makes actions modular
 * callback(eventName, value, subscriberIdentifier)
 * setup
 * shutdown
 * subscribers should have a strategy (randomize or wait)
 * maybe a priority (1-10)

NaoqiProvider - triggered by Nao's API
 * add_subscriber
 * enable / disable callbacks
 * setup & shutdown
 * event_callback (private)

DaemonProvider - trigger by a forked background process
 * concerns: look at time of day, last recog person, lighting, awake time, etc.
 ** add_subscriber
 ** enable / disable 
 ** setup / shutdown
 ** callback on subscribers

## Services

Logging
 * rails / REST

Vocabulary
 * rails / REST

Movement
 * naoscripts that can be used

# Notes on abstract class in python

```
from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass

Abstract()
>>> TypeError: Can not instantiate abstract class Abstract with abstract methods foo

class B(Abstract):
    pass

B()
```