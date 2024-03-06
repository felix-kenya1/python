#salary calculation
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary method")

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, salary, monthly_salary):
        super().__init__(emp_id, name, salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

hourly_emp = HourlyEmployee(1, "John Doe", 0, 20, 40)
print(hourly_emp.calculate_salary())  # Output: 800

salaried_emp = SalariedEmployee(2, "Jane Doe", 0, 3000)
print(salaried_emp.calculate_salary())  # Output: 3000