from replit import db
from employee import Employee
from employee_repository import EmployeeRepository


class EmployeeRepositoryReplitDb(EmployeeRepository):
    def all(self) -> [Employee]:
        return (db[employee_id] for employee_id in db.keys())

    def get_by_id(self, employee_id: str) -> Employee:
        if db.get(employee_id):
            return Employee(db.get(employee_id))
        raise KeyError(employee_id)


class ReplitRepoFactory:
    @staticmethod
    def get_repo() -> EmployeeRepository:
        return EmployeeRepositoryReplitDb()