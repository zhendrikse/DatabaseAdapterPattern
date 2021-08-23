from fastapi import FastAPI
import uvicorn
from repository import ReplitDbEmployeeRepository, Employee
from employee_endpoint import EmployeeEndPoint


app = FastAPI()
endpoint = EmployeeEndPoint(ReplitDbEmployeeRepository())

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employee")
def list_all_employees():
  return endpoint.get_all_employees()

# @app.put("/employee")
# def add_new_employee(employee: Employee, employee_id: str):
#   endpoint.add_employee(employee, employee_id)

uvicorn.run(app,host="0.0.0.0",port=8080)