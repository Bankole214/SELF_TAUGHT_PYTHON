# python has functions for creating , reading , updating and deleting files 

# Open a file 
myFile = open('myfile.txt', 'w')

# Get some info 
print('name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)




# Write to file

myFile.write('i love python')
myFile.write(' i love java')
myFile.close()



#Append to file 

myFile = open('myfile.txt', 'a')
myFile.write(' and honestly i don\'t like C')



# Read from a file

myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)