from repository import ReplitDbEmployeeRepository, EmployeeRepository, Employee

class EndPoint():
  def __init__(self, employeeRepo: EmployeeRepository):
    self.employeeRepository = employeeRepo

  def get_all_employees(self) -> [Employee]:
    return self.employeeRepository.all()

#app = EndPoint(ReplitDbEmployeeRepository)

