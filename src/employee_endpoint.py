from repository import EmployeeRepository, Employee

class EmployeeEndPoint():
  def __init__(self, employeeRepo: EmployeeRepository):
    self.employeeRepository = employeeRepo

  def get_all_employees(self) -> [Employee]:
    return self.employeeRepository.all()

  def number_of_employees(self) -> int:
    return self.employeeRepository.size()

  def get_employee_by_id(self, employee_id:str) -> Employee:
    return self.employeeRepository.get_by_id(employee_id)

  def add_employee(self, new_employee:Employee, employee_id:str) -> None:
    self.employeeRepository.add(new_employee, employee_id)


