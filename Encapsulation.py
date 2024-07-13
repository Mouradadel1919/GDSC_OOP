# #                                         Public Attributes
#
# class Student:
#     def __init__(self, name):
#         self.name= name
#
# student1= Student("mo")
# print(student1.name)
# student1.name= "mohaamed"
# print(student1.name)


###                                        Protected Attributes
# class Student:
#     def __init__(self, name, serial):
#         self.name = name
#         self._serial = serial
#
#     def get_serial(self):
#         return self._serial
#
#     def set_serial(self, value):
#         self._serial = value
#         return self._serial
# class Branch(Student):
#     pass
#
#
#
############ Do not use Protected things outside the Parernt & derived classes  ############
############ so do not use this way to deal with protected Things   ######
#
# b1= Branch("Tarek", 98)
# print(b1._serial)
# b1._serial= 77
# print(b1._serial)
#
# #          ############               Use This Way                       ############
#
# print(b1.get_serial())
# b1.set_serial(10)
# print(b1.get_serial())


##                                       Private Attributes
#
#
# # class Student:
# #     def __init__(self, name, serial, password):
# #         self.name = name
# #         self._serial = serial
# #         self.__password = password
#
#     # def get_password(self):
#     #     return self.__password
#     #
#     # def set_password(self, value):
#     #     self.__password = value
#     #     return self.__password

############ You can not use private things outside their class OR any other Classes ############

# student1= Student("mo", 202, 55)
# print(student1.__password)


#
# class Branch(Student):
#     pass

# #          ############ You can not use private things outside their class OR any other Classes ############

# b1= Branch("Tarek", 98, "khh")
# # print(b1.__password)
# b1.__password = "5555"
# print(b1.__password)



# #          ############               Use This Way                       ############


# b1= Branch("Tarek", 98, "khh")
# print(b1.get_password())
# b1.set_password("dffgfdgd10")
# print(b1.get_password())


# #          ############               Name Mangling                     ############

# print(student1._Student__password)

