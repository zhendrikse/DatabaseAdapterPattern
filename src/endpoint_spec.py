from mamba import description, it, context, before
from expects import expect, equal, have_len, raise_error
from fastapi import HTTPException
from employee import Employee

from endpoint import EmployeeEndpoint

with description(EmployeeEndpoint) as self:
  with before.each:
    self.endpoint = EmployeeEndpoint()

  with context("Health service endpoint"):
    with it("returns pong after ping"):
      expect(self.endpoint.ping()).to(equal("Pong"))

  with context("Employee endpoint"):
    with it("lists all employees"):
      expect(self.endpoint.list_employees()).to(have_len(3))

    with it ("throws an exception if Emplyee ID does not exist"):
      expect(lambda: self.endpoint.get_employee_by_id("_non-existent-id_")).to(raise_error(HTTPException))