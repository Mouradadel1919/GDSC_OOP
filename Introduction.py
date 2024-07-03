class Employee:

    #class Attribute
    num_of_emp = 10

    #constructor
    def __init__(self, names, age):
        #instance Attributes & object Attributes

        self.name = names
        self.age = age


    #instance Method
    def print_info(self):
        print(f"{self.name}, {self.age} ")
        print(Employee.num_of_emp)


    #decorator
    @classmethod
    def print_num(cls):
        print(cls.num_of_emp)
        print(Employee.num_of_emp)

    @staticmethod
    def print_hi():
        print("hi")






emp1 = Employee("mourad" , 20)
emp1.print_hi()
Employee.print_hi()













