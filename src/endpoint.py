from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import uvicorn

from repository import ReplitDbEmployeeRepository, EmployeeRepository
from employee import Employee

app = FastAPI()
router = InferringRouter()

def get_repo() -> EmployeeRepository:
  return ReplitDbEmployeeRepository()

@cbv(router) 
class EmployeeEndpoint:
    @router.get("/")
    def ping(self) -> str:
       return 'Pong'

    @router.get("/employees")
    def list_all_employees(self, repo: EmployeeRepository = Depends(get_repo)):
      return repo.all()

    @router.get("/employees/{employee_id}")
    def get_employee_by_id(self, employee_id: str, repo: EmployeeRepository = Depends(get_repo)):
      try:
        return repo.get_by_id(employee_id)
      except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    @router.delete("/employees/{employee_id}")
    def delete_employee(self, employee_id: str, repo: EmployeeRepository = Depends(get_repo)):
      try:
        return repo.delete(employee_id)
      except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    @router.put("/employees", status_code=201)
    def add_new_employee(self, name: str, employee_id: str, repo: EmployeeRepository = Depends(get_repo)):
      repo.add(Employee(name), employee_id)
