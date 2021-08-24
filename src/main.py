from fastapi import FastAPI, HTTPException
import uvicorn
from repository import ReplitDbEmployeeRepository
from controller import Controller
from employee import Employee


app = FastAPI()
controller = Controller(ReplitDbEmployeeRepository())

class EmployeeEndpoint():
  @app.get("/")
  async def read_root():
      return {"Status": "Up"}

  @app.get("/employees")
  async def list_all_employees():
    return controller.get_all_employees()

  @app.get("/employees/{employee_id}")
  async def get_employee_by_id(employee_id: str):
    try:
      return controller.get_employee_by_id(employee_id)
    except KeyError:
      raise HTTPException(status_code=404, detail="Item not found")

  @app.put("/employees", status_code=201)
  def add_new_employee(name: str, employee_id: str):
    controller.add_employee(Employee(name), employee_id)

uvicorn.run(app,host="0.0.0.0",port=8080)