from replit import db
from employee import Employee
from abc import ABC,abstractmethod


class EmployeeRepository(ABC):
  @abstractmethod
  def all(self) -> [Employee]: pass

  @abstractmethod
  def get_by_id(self, id: str) -> Employee: pass

  @abstractmethod
  def add(self, new_employee:Employee, employee_id:str) -> None: pass

  @abstractmethod
  def delete(self, id:str) -> None: pass


class StubEmployeeRepository(EmployeeRepository):
  def __init__(self):
    self.employees_by_id = {
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

  def delete(self, id: str) -> None:
    self.employees_by_id.pop(id)

class ReplitDbEmployeeRepository(EmployeeRepository):
  def all(self) -> [Employee]:
    return (db[employee_id] for employee_id in db.keys())

  def get_by_id(self, id: str) -> Employee:
    if db.get(id):
      return Employee(db.get(id))
    raise KeyError(id)

  def add(self, new_employee:Employee, employee_id: str) -> None:
    db[employee_id] = new_employee.name

  def delete(self, employee_id: str) -> None:
    del db[employee_id]
  
  # def toJson(self):
  #   return json.dumps(self, default=lambda o: o.__dict__)

class StubRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return StubEmployeeRepository()

class ReplitRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return ReplitDbEmployeeRepository()