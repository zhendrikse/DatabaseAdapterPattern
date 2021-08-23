from replit import db

class Employee():
  def __init__(self, name: str):
    self.name = name
          
  def __eq__(self, other): 
      if not isinstance(other, Employee):
          return NotImplemented

      return self.name == other.name # and self.bar == other.bar


class EmployeeRepository():
  def size(self) -> int: pass

  def all(self) -> [Employee]: pass

  def get_by_id(self, id: str) -> Employee: pass

  def add(self, new_employee:Employee, employee_id:str) -> None: pass


class StubEmployeeRepository(EmployeeRepository):
  employees_by_id = {
    "001": Employee("Zeger"),
    "002": Employee("Atharva"),
    "003": Employee("Misbah") 
  }

  def size(self) -> int:
    return len(self.employees_by_id)

  def all(self) -> [Employee]:
    return self.employees_by_id.values()

  def get_by_id(self, id: str) -> Employee:
    return self.employees_by_id[id];

  def add(self, new_employee:Employee, employee_id: str) -> None:
    self.employees_by_id[employee_id] = new_employee


class ReplitDbEmployeeRepository(EmployeeRepository):
  def size(self) -> int:
    return len(db)

  def all(self) -> [Employee]:
    return db.values()

  def get_by_id(self, id: str) -> Employee:
    return db[id];

  def add(self, new_employee:Employee, employee_id: str) -> None:
    db[employee_id] = new_employee

