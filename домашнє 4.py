class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} — {self.position}, ЗП: {self.salary} грн"


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, name: str):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def get_total_salary(self) -> int:
        return sum(emp.salary for emp in self.employees)

    def display_employees(self):
        if not self.employees:
            print(f"У відділі '{self.name}' немає співробітників.")
            return
        print(f"Співробітники відділу '{self.name}':")
        for emp in self.employees:
            print(f"- {emp}")
        print(f"Загальна заробітна плата відділу: {self.get_total_salary()} грн")


emp1 = Employee("Олексій", "Розробник", 50000)
emp2 = Employee("Марія", "Дизайнер", 45000)
emp3 = Employee("Іван", "Менеджер", 40000)

dept = Department("IT Відділ")

dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)

dept.display_employees()

dept.remove_employee("Іван")
dept.display_employees()