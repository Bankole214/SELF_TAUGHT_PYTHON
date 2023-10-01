#  LOOP --- IS USED FOR ITERATING OVER A SEQUENCE (THAT IS EITHER A LIST[],TUPLE(), A DIC {}, A SET OR A STRING "")


people = ['john','alia','aisha','dan']

#simple FOR LOOP
# for person in people:
#     print(f'current person: {person}')


# BREAK    break the loops when it gets to the conditions stated #aisha

# for person in people:
#     if person == 'aisha':
#         break
#     print(f'current person: {person}')



#    CONTINUE         skips the condition AISHA and continue the list

# 
# for person in people:
#     if person == 'aisha':
#         continue
#     print(f'current person: {person}')

#    RANGE    

# for i in range(len(people)):
#     print(people[i])


# for i in range(0,11):
#     print(f'number: {i}')




#   WHILE loops EXECUTES A SET OF STATEMENTS AS LONG AS A CONDITIONSNIS TRUE
count = 0
while count <= 10:
    print(f'count: {count}')
    count += 1