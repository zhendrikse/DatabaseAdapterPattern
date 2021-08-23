from mamba import description, it, context, before
from expects import expect, equal
from repository import StubEmployeeRepository, Employee
from employee_endpoint import EmployeeEndPoint

with description(EmployeeEndPoint) as self:

  with context("Given a new repository"):
    with before.each:
      self.endpoint = EmployeeEndPoint(StubEmployeeRepository())

    with context("When querying the size"):
      with it("should return three"):
        expect(len(self.endpoint.get_all_employees())).to(equal(3))

    with context("When querying all employees"):
      with it("should return all employee records"):
        expect(self.endpoint.number_of_employees()).to(equal(3))  
  
    with context("When querying by ID"):
      with it("should return the employee with given ID"):
        expect(self.endpoint.get_employee_by_id("001")).to(equal(Employee("Zeger")))
      with it("should throw an exception when ID does not exist"):
        try:
          self.endpoint.get_employee_by_id('xxx')
          raise("Non-existing employee should not be found")
        except:
          pass

    with context("When adding a new employee"):
      with it("should have four entries"):
        self.endpoint.add_employee(Employee("Jan"), "004")
        expect(self.endpoint.number_of_employees()).to(equal(4))
