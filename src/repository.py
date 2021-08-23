from replit import db
from employee import Employee

class EmployeeRepository():
  def all(self) -> [Employee]: pass

  def get_by_id(self, id: str) -> Employee: pass

  def add(self, new_employee:Employee, employee_id:str) -> None: pass


class StubEmployeeRepository(EmployeeRepository):
  employees_by_id = {
    "001": Employee("Zeger"),
    "002": Employee("Atharva"),
    "003": Employee("Misbah") 
  }

  def all(self) -> [Employee]:
    return self.employees_by_id.values()

  def get_by_id(self, id: str) -> Employee:
    return self.employees_by_id[id]

  def add(self, new_employee:Employee, employee_id: str) -> None:
    self.employees_by_id[employee_id] = new_employee


class ReplitDbEmployeeRepository(EmployeeRepository):
  def all(self) -> [Employee]:
    employees = []
    for employee_id in db.keys():
      employees.append(db[employee_id])
    return employees

  def get_by_id(self, id: str) -> Employee:
    name = db.get(id)
    if name:
      return Employee(db.get(id))
    raise KeyError(id)

  def add(self, new_employee:Employee, employee_id: str) -> None:
    db[employee_id] = new_employee.name

