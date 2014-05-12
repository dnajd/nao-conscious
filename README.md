# Nao Conscious

Have Nao seem conscious. Meaning aware of and responding to one's surroundings; awake.


# Abstractions

Built an event management system where subscribers are registered with event providers.

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