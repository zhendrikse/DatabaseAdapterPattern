from fastapi import FastAPI, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import uvicorn

from repository import ReplitDbEmployeeRepository
from controller import Controller
from employee import Employee

app = FastAPI()
router = InferringRouter()

@cbv(router) 
class EmployeeEndpoint:
    def __init__(self, custom_controller = Controller(ReplitDbEmployeeRepository())):
      self.controller = custom_controller

    @router.get("/")
    def ping(self) -> str:
       return 'Pong'

    @router.get("/employees")
    async def list_all_employees(self):
      return self.controller.get_all_employees()

    @router.get("/employees/{employee_id}")
    async def get_employee_by_id(self, employee_id: str):
      try:
        return self.controller.get_employee_by_id(employee_id)
      except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    @router.put("/employees", status_code=201)
    def add_new_employee(self, name: str, employee_id: str):
      self.controller.add_employee(Employee(name), employee_id)

app.include_router(router)
uvicorn.run(app,host="0.0.0.0",port=8080)
