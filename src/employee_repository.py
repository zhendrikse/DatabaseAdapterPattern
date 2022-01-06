from employee import Employee
from abc import ABC, abstractmethod


class EmployeeRepository(ABC):
    @abstractmethod
    def all(self) -> [Employee]: pass

    @abstractmethod
    def get_by_id(self, id: str) -> Employee: pass
