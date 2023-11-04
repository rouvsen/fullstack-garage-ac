class Employee(object):
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount
        return self.emp_salary

    def assign_emp_department(self, department):
        self.emp_department = department

    def print_employee_details(self):
        print(f"""
            id: {self.emp_id},
            name: {self.emp_name},
            salary: {self.emp_salary},
            department: {self.emp_department}
        """)

adams = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
jones = Employee("E7499", "JONES", 45000, "RESEARCH")
martin = Employee("E7900", "MARTIN", 50000, "SALES")
smith = Employee("E7698", "SMITH", 55000, "OPERATIONS")

adams.print_employee_details()
# jones.print_employee_details()
# martin.print_employee_details()
# smith.print_employee_details()

sal = adams.calculate_emp_salary(200)

adams.print_employee_details()