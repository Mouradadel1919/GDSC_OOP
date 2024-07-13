#                                      #Method Overloading

# class Demo:
#     def add(self, n1, n2):
#         return n1 + n2
#

#     def add(self, n1, n2, n3):
#         return n1+ n2+ n3
#
#
# d1= Demo()
# print(d1.add(1, 5, 6))

# class Demo:
#     def add(self, *args):
#         total= 0
#         for num in args:
#             total += num
#         return total
#
#
# demo1= Demo()
# print(demo1.add(10, 20, 50, 7, 6, 8))
# print(demo1.add(10, 20, 50))
#
#
# #                                      #Method Overriding
#
class Human:

    def eat(self):
        print("i Can eat")

    def work(self, num):
        print("i Can work")

class child(Human):

    def play(self):
        print("i can play")
    def work(self):
        super().work(10)
        print("i Can code")

ch1 = child()
ch1.work()