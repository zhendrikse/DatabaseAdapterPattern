from mamba import description, it, context, before
from expects import expect, equal
from repository import EmployeeRepository, StubEmployeeRepository, Employee

with description(EmployeeRepository) as self:

  with context("Given a new repository"):
    with before.each:
      self.employeeRepository = StubEmployeeRepository()

    with context("When querying the size"):
      with it("should return three"):
        expect(len(self.employeeRepository.all())).to(equal(3))

    with context("When querying all employees"):
      with it("should return all employee records"):
        expect(len(self.employeeRepository.all())).to(equal(3))  
  
    with context("When querying by ID"):
      with it("should return the employee with given ID"):
        expect(self.employeeRepository.get_by_id("001")).to(equal(Employee("Zeger")))
      with it("should throw an exception when ID does not exist"):
        try:
          self.employeeRepository.get_by_id('xxx')
          raise("Non-existing employee should not be found")
        except:
          pass

    with context("When adding a new employee"):
      with it("should have four entries"):
        self.employeeRepository.add(Employee("Jan"), "004")
        expect(self.employeeRepository.size()).to(equal(4))
