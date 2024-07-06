class Father:
    def __init__(self, name):
        self.hair = "Black"
        self.eyes = "Brown"
        # self.name = name

    def eat(self):
        print("Father can eat")

    def work(self):
        print("Father can work")


class Mother:
    def __init__(self):
        self.hair = "Blonde"
        self.eyes = "Green"

    def play(self):
        print("Mom can play")

    # Method Overriding
    def work(self):
        print("Mom can work")


class Child(Father, Mother):

    def __init__(self, name, age):
        Mother.__init__(self)
        Father.__init__(self, name)          # self.name = name
        self.age = age
    #     # self.hair = "......."
    #     # self.eyes = "......."



    def work(self):
        Mother.work(self)  # = print("Mom can work")
        super().work()
        # Father.work(self)  # = super().work()
        print("I know OOP")


ch1 = Child("Ali", 25)
ch1.work()
print(ch1.eyes, ch1.hair)
print(ch1.age)
