# Nao Conscious

Have Nao seem conscious. Meaning aware of and responding to one's surroundings; awake.


# Abstractions

Built an event management system where subscribers are registered with event providers.

## Subscribers

Make nao's actions modular; ex. log an event, say something, move.
* callback(eventName, value, subscriberIdentifier)
* setup()
* tear_down()

## Providers

Can be assigned subscribers and trigger them at will
* add_subscriber(subscriber)
* setup()
* tear_down()