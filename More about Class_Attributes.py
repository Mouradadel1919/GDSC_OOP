class Employee:
    employee_num = 0  # Class Attributes     self.employee_num = 2

    @staticmethod  # decorator
    def info():  # staticmethod
        print("Hello .. You are in Employee Class")

    @classmethod  # decorator
    def emp_num_plus_for_class(cls, num):
        cls.employee_num += num

    def emp_num_plus_for_object(self, num):
        self.employee_num += num

    def __init__(self):
        self.info()

        self.emp_num_plus_for_class(1)  # Class Method      # = Employee.employee_num += 1        (OK)
        self.emp_num_plus_for_object(1)  # Instance Method   # = self.employee_num += 5            (NO)
        self.emp_num_plus_for_class(1)  # Class Method      # = Employee.employee_num += 1        (OK)


obj1 = Employee()

print(Employee.employee_num)
print(obj1.employee_num)
print(Employee.employee_num)
