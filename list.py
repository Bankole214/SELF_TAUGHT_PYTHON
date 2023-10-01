number = [0, 1, 2, 3, 4, 5]
fruits = ['apple','orange','grape','pear']




#use a constructor
#number2 = list((1, 2, 3, 4,5))


#GET A VALUE
print(fruits[3])

#GET LENGTH
print(len(fruits))

#append to list)
fruits.append('carrot')



#remove/replace from the list
fruits.remove('pear')

#insert into the list at a position
fruits.insert(1, 'cashew')


#remove with pop without replacement
fruits.pop(2)

#reverse the list
fruits.reverse()

#sort the list
fruits.sort()

#reverse sort the list
#fruits.sort(reverse=True)

#change value
fruits[0] = 'blueberry'

print(fruits)