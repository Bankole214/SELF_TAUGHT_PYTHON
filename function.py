#CREATE A FUNCTION

def sayHello(name = 'Dimsey'):
    print(name)

sayHello()


#RETURN VALUE

def getSum(num1,num2):
    total = num1 + num2
    return total

#print (getSum(20,10))




#lamda function  is a small aninymous function that
getSum = lambda num1,num2: num1 + num2

print (getSum(20,10))


