# Nao Event Management

Event management system for writing code as subscribers and registering them with event providers.


# Abstractions

Phase I. Start with providers calling subscribers directly. No thread safety.

## Subscribers

Make nao's actions modular; ex. log an event, say something, move.

* callback(eventName, value, subscriberIdentifier)
* setup
* shutdown
* base subscriber class that...
    * subscribers should have a strategy (randomize or wait)
    * maybe a priority (1-10)
    * cool down probability

## Providers

NaoqiProvider - wrapper for naoqi events
* add_subscriber
* enable / disable callbacks
* setup & shutdown
* event_callback (private)

DaemonProvider - forked background process; nao conciousness
* Concerns - look at time of day, last recog person, lighting, awake time, etc.
    * add_subscriber
    * enable / disable 
    * setup / shutdown
    * callback on subscribers

## Consider

Consider having a Command Queue
 * Providers hand subscribers over to the command queue to be executed
 * Command Queue figures out blocking vs non-blocking
 * Also can contain nao's state or anything we want to remember out what's going on with nao

# Look at Wanderer

https://github.com/davesnowdon/nao-wanderer/blob/master/wanderer/src/main/python/wanderer/wanderer.py

* Planner
* PlanExecutor

https://github.com/davesnowdon/nao-wanderer/blob/master/wanderer/src/main/python/wanderer/event.py


# OLD OLD OLD

The things below belogn in another project

Make nao seem alive

* Focus on unpredictability & randomness; the essence of life
* With a hint of logic
* Architecture for experimenting with autonomy

# Project Name

* marionette

# Idea's

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

Memory

* talk about what just happened; hey joe, john was just here 5 minutes ago

# Architecture & Notes

## Required Services

Logging

 * REST service that can store event history

Vocabulary

 * vocab word and response; either text or naoscript

Movement

 * Naoscripts that can be triggered by a naoscript subscriber

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