# Goal

This projects demonstrates how to implement an adapter pattern in Python so that the system under test (SUT) can be tested locally, i.e. all adapters can be stubbed when running the SUT locally.

## Implementation

The implementation uses a Replit DB as storage for simple Employee records. The calls to the Replit DB have been implemented using an adapter, so that the calls to the Replit DB can easily be isolated during (unit) testing.

The endpoint is implemented using the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) framework.