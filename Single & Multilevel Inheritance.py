class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can work")

#Single Inheritance
class Male(Person):
    def __init__(self, name, salary, age):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.salary = salary

    #Methods
    def play(self):
        print("I can play")

    def work(self):
        print("I can code")
        super().work()

    def display(self):
        return f"My name is {self.name}, I have {self.salary} Pounds"


###############################################################
male1 = Male("mourad", 10000, 50)
male1.eat()
male1.play()
male1.work()
print(male1.display())
print(60 * "*")


#Multilevel Inheritance
class Female(Male):
    def __init__(self, name, salary, age, gpa):
        Male.__init__(self, name, salary, age)
        # self.name = name
        # self.salary = salary
        # self.age = age

        self.gpa = gpa


female1 = Female("sara", 15000, 1, 3)
print(female1.display())
female1.eat()
female1.play()
female1.work()







