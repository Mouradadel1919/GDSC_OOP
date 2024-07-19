from abc import ABCMeta, abstractmethod
class Animals(metaclass= ABCMeta): #no object & must use our methods
    @abstractmethod
    def getsound(self):
        pass

# an1 =Animals()
class cats(Animals):
    def getsound(self):
        return "cat sound"

cat1 = cats()
print(cat1.getsound())

# class dogs(Animals):
#     def getsound(self):
#         return "dog sound"

# dog1 = dogs()