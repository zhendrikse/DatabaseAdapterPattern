from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from employee_repository_replit_db import ReplitRepoFactory, EmployeeRepository

app = FastAPI()
router = InferringRouter()
repository = ReplitRepoFactory.get_repo


@cbv(router)
class EmployeeEndpoint:
    @router.get("/")
    def ping(self) -> str:
        return 'Pong'

    @router.get("/employees")
    def list_all_employees(self, repo: EmployeeRepository = Depends(repository)):
        return repo.all()

    @router.get("employees/{employee_id}")
    def get_employee_by_id(self, 
                           employee_id: str, 
                           repo: EmployeeRepository = Depends(repository)):
        try:
            repo.get_by_id(employee_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Employee not found")
