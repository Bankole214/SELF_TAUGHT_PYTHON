#   A CLASS is like a bblueprint for creating objects.An object has properties and methods(funcs) associated with it. Almost everything in python is an object


#  create a class
class User:
    #constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age


#creating a method
    def greeting(self):
        return f'my name is {self.name} and i am {self.age}'
    

    def has_birthday(self):
        self.age += 1



# Extend Class 

class Customer(User):
        #constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0


    def set_balance(self,balance):
        self.balance = balance

    def greeting(self):
        return f'my name is {self.name} and i am {self.age} and my balance is {self.balance}'



#init user object

dimsey = User('Dimsey','dimsey214@gmail.com',21)


#init customer object 
amirah = Customer('amirah jimoh','amira@gmail.com',19)

amirah.set_balance(100)
print(amirah.greeting())

dimsey.has_birthday()
print(dimsey.greeting())   



#print(dimsey.age)   #list/access element in a class
#print(type(dimsey))