# Goal

This project demonstrates how to implement an adapter pattern in Python so that the system under test (SUT) can be tested _locally_. Here, the SUT is a simple API that retrieves very basic employee data from a database.

This example illustrates [Data Access/Adapter Logic](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic/#2-Data-Access--Adapter-Logic) as discussed in [Organizing App Logic with the Clean Architecture](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic).

## Quircks

Before you can do anything at all, you must run in the shell the following command:

```
$ pip install fastapi_utils
```

## Implementation

The implementation uses a [Replit DB](https://docs.replit.com/tutorials/11-using-the-replit-database) as storage for simple [Employee](https://replit.com/@zwh/DatabaseAdapterPattern#src/repository.py) records. The calls to the Replit DB have been implemented using an adapter/repository, so that the calls to the Replit DB can easily be isolated during (unit) testing.

The endpoint has been implemented using the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) framework.

The tests have been written in an BDD-style using [Mamba](https://github.com/nestorsalceda/mamba): the definitive test runner for Python in combination with [expects](https://expects.readthedocs.io/en/stable/#).

## Running the tests

The project is configured in such a way, that by pressing the "Run" button, the unit tests are executed.

## Running the application

In the shell, go to the ``src`` folder and enter
```
$ python main.py
```

You can reach the endpoint by appending /docs to the given URL (https://DatabaseAdapterPattern.zwh.repl.co).
