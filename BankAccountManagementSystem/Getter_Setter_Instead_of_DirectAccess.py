"""
How do getters and setters relate?
Term	Role in Encapsulation
Getter	Allows controlled access to private/protected attributes
Setter	Allows controlled modification of private/protected attributes

They prevent external code from directly modifying internal state unless the change is valid.
"""

class Employee:
    def __init__(self, name, salary):
        self._name = name            # protected
        self.__salary = salary       # private

    @property
    def salary(self):
        return self.__salary         # Getter

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("❌ Salary cannot be negative")
        self.__salary = value        # Setter

e = Employee("Jyoti", 50000)
print(e.salary)      # ✅ Access through getter

e.salary = 60000     # ✅ Set through setter
# e.salary = -500     # ❌ Raises ValueError


