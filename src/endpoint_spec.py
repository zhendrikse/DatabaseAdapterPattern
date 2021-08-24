from mamba import description, it, context, before
from expects import expect, equal

from fastapi import HTTPException

from endpoint import EmployeeEndpoint
from repository import StubRepoFactory
from employee import Employee

with description(EmployeeEndpoint) as self:
  with context("Given an employee endpoint"):
    with before.each:
      self.repo = StubRepoFactory.get_repo()
      self.endpoint = EmployeeEndpoint()

    with context("When inovking GET on /employees"):
      with it("should return three"):
        expect(
          len(self.endpoint.list_all_employees(repo=self.repo))).to(equal(3))
    
    with context("When invoking GET on /employees with ID"):
      with it("should return the employee with given ID"):
        expect(
          self.endpoint.get_employee_by_id("001", repo=self.repo)).to(equal(Employee("Zeger")))

      with it("should throw an exception when ID does not exist"):
        try:
          self.endpoint.get_employee_by_id("xxx", repo=self.repo)
          raise("Non-existing employee should not be found")
        except HTTPException:
          pass

    with context("When invoking PUT on /employee"):
      with it("should have added the new employee"):
        self.endpoint.add_new_employee("Jan", "004", repo=self.repo)
        expect(
          len(self.endpoint.list_all_employees(repo=self.repo))).to(equal(4))
        expect(
          self.endpoint.get_employee_by_id("004", repo=self.repo)).to(equal(Employee("Jan")))

    with context("When inovking DELETE on /employees"):
      with it("should throw an exception when ID does not exist"):
        try:
          self.endpoint.delete_employee("xxx", repo = self.repo)
          raise("Non-existing employee should not be found")
        except HTTPException:
          pass

      with it("should have two employees left"):
        self.endpoint.delete_employee("003", repo=self.repo)
        expect(
          len(self.endpoint.list_all_employees(repo=self.repo))).to(equal(2))
