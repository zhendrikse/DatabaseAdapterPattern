from fastapi import FastAPI
import uvicorn
from repository import ReplitDbEmployeeRepository, Employee
from endpoint import EndPoint


app = FastAPI()
endpoint = EndPoint(ReplitDbEmployeeRepository())

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/all")
def all():
  return endpoint.get_all_employees()

uvicorn.run(app,host="0.0.0.0",port=8080)