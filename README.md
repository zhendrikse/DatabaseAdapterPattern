# Goal

This projects demonstrates how to implement an adapter pattern in Python so that the system under test (SUT) can be tested locally, i.e. all adapters can be stubbed when running the SUT locally.

## Implementation

The implementation uses a [Replit DB](https://docs.replit.com/tutorials/11-using-the-replit-database) as storage for simple [Employee](https://replit.com/@zwh/DatabaseAdapterPattern#src/repository.py) records. The calls to the Replit DB have been implemented using an adapter, so that the calls to the Replit DB can easily be isolated during (unit) testing.

The endpoint is implemented using the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) framework.

## Running the tests

The project is configured in such a way, that by pressing the "Run" button, the unit tests are executed.

## Running the application

In the shell, go to the ``src`` folder and enter
```
$ python main.py
```
 
