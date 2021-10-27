# Goal

## General introduction

This project demonstrates how to implement an adapter pattern in Python so that the system under test (SUT) can be tested _locally_. Here, the SUT is a simple API that retrieves very basic employee data from a database.

This example illustrates [Data Access/Adapter Logic](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic/#2-Data-Access--Adapter-Logic) as discussed in [Organizing App Logic with the Clean Architecture](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic).

## Hexagonal/clean architecture

The general idea here is to isolate all of your external dependencies explicitly by bundling all communication in so-called adapters that are conceptually located the [onion layer](https://www.codeguru.com/csharp/understanding-onion-architecture/) surrounding the domain model:

![Hexagonal architecture](./hex_arch.draw)

This is also closely related to the [dependency inversion principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle), where we make the external systems comply with our domain model and not the other way around. 

By employing an hexagonal architecture, we can still test all our domain logic locally by pluggin in test doubles at the adapters like so:

![Testing with adapters](./hex_arch_unit.draw)

### Further reading

Be sure to check out this excellent read called [DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together](herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/). But it is also wise to keep in mind what Mark Seemann states: [Layers, Onions, Ports, Adapters: it's all the same](https://blog.ploeh.dk/2013/12/03/layers-onions-ports-adapters-its-all-the-same/). 


## About this example 

### Description

This is a very basic example API that stores and retrieves employee data.

### Quircks

Before you can do anything at all, you must run in the shell the following command:

```
$ pip install fastapi_utils
```

### Implementation details

The implementation uses a [Replit DB](https://docs.replit.com/tutorials/11-using-the-replit-database) as storage for simple [Employee](https://replit.com/@zwh/DatabaseAdapterPattern#src/repository.py) records. The calls to the Replit DB have been implemented using an adapter/repository, so that the calls to the Replit DB can easily be isolated during (unit) testing.

The endpoint has been implemented using the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) framework.

The tests have been written in an BDD-style using [Mamba](https://github.com/nestorsalceda/mamba): the definitive test runner for Python in combination with [expects](https://expects.readthedocs.io/en/stable/#).

### Running the tests

The project is configured in such a way, that by pressing the "Run" button, the unit tests are executed.

### Running the application

In the shell, go to the ``src`` folder and enter
```
$ python main.py
```

You can reach the endpoint by appending /docs to the given URL (https://DatabaseAdapterPattern.zwh.repl.co).


