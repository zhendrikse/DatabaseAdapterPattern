from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from employee import Employee

app = FastAPI()
router = InferringRouter()

@cbv(router)
class EmployeeEndpoint:
  @router.get("/")
  def ping(self) -> str:
    return 'Pong'

  @router.get("/employees")
  def list_employees(self):
    return [Employee("Mark"), Employee("John"), Employee("Darren")]

  @router.get("/employees/{employee_id}")
  def get_employee_by_id(self, employee_id: str):
    raise HTTPException(status_code=404, detail="Employee not found")
