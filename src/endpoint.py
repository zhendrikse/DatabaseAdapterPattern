from fastapi import FastAPI, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import uvicorn

from repository import ReplitDbEmployeeRepository
from employee import Employee

app = FastAPI()
router = InferringRouter()

@cbv(router) 
class EmployeeEndpoint:
    def __init__(self, repository = ReplitDbEmployeeRepository()):
      self.repo = repository

    @router.get("/")
    def ping(self) -> str:
       return 'Pong'

    @router.get("/employees")
    def list_all_employees(self):
      return self.repo.all()

    @router.get("/employees/{employee_id}")
    def get_employee_by_id(self, employee_id: str):
      try:
        return self.repo.get_by_id(employee_id)
      except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    @router.delete("/employees/{employee_id}")
    def delete_employee(self, employee_id: str):
      try:
        return self.repo.delete(employee_id)
      except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    @router.put("/employees", status_code=201)
    def add_new_employee(self, name: str, employee_id: str):
      self.repo.add(Employee(name), employee_id)
