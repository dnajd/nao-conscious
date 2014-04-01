# Goals

* Autonomy
* Sociability
* Fun

# Features

Eye contact with people

 * using the face tracker for the most basic social tactic

Face Recognition
 * log: who, when & how many time
 * express familiarity through warm / cold greetings based on stats
 * even add predictability with stats; ex. someone should be here right now

Word Recognition
 * library of responses to build vocabulary

Movement
 * random movement to express vitality
 * triggered movement based on: time of day, face recognition, sound localization, word recognition

Probability
 * give events a probability of happening or not
 * used to choose between multiple possible events / actions
 * used to create a sense of identity, preference, personality

# Architecture

## Wrappers

Deal with thread safty, modularity & event management

Subscribers
 * callback(eventName, value, subscriberIdentifier)
 * setup
 * shutdown

FaceRecognition (and others)
 * add_subscriber
 * start_callback
 * stop_callback
 * event_callback

Daemon
 * trigger subscribers based on cycle / last run
 * subscribers should have a strategy (randomize or wait) and maybe a priority (1-10)

Logging
 * rails / REST

Vocabulary
 * rails / REST



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