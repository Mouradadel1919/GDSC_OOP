from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def printall(self):
        pass

class Employee(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self._salary = salary

    def setsalary(self, num):
        self._salary = num

    def getsalary(self):
        return self._salary

    def printall(self):
        return self.name, self.age, self.gender, self._salary


#############################################################
# em1 = Employee("Ali", 20, "Male", 10000)
# print(em1.printall())
# em1.setsalary(50000)
# print(em1.getsalary())
#############################################################
class Manager(Person):
    def __init__(self, name, iid, location):
        self.name = name
        self.id = iid
        self.location = location

    def printall(self):
        return self.name, self.id, self.location


#######################################################
# man1 = Manager("Ali", "15E", "Menofia")
# print(man1.printall())
#######################################################

class CEO(Manager, Employee):

    def __init__(self, name, iid, location, age, gender, salary, password):
        Manager.__init__(self, name, iid, location)
        Employee.__init__(self, name, age, gender, salary)
        self.__password = password

    def __printinfo(self):  # Method Override
        return self.name, self.id, self.location, self.age, self.gender, self._salary

    def printall(self):
        if self.__password == "1234":
            print(self.__printinfo())
        else:
            print("Password is incorrect")
##########################################################################
# ceo1 = CEO("Ali", "20h", "street1", 20, "male", 10000, "1234")
# ceo1.printall()
##########################################################################
