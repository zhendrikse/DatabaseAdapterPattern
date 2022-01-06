from employee_repository import EmployeeRepository
from employee import Employee


class EmployeeRepositoryStub(EmployeeRepository):
    def __init__(self):
        self.employees_by_id = {
            "001": Employee("Darren"),
            "002": Employee("Atharva"),
            "003": Employee("Misbah")
        }

    def all(self) -> [Employee]:
        return self.employees_by_id.values()

    def get_by_id(self, employee_id: str) -> Employee:
        print(employee_id)
        employee = self.employees_by_id[employee_id]
        print(employee)
        return employee


class RepoStubFactory:
    @staticmethod
    def get_repo() -> EmployeeRepository:
        return EmployeeRepositoryStub()
