#  IF/ELSE CONDITION ARE USED TO DECIDE TO DO SOMETHING BASED ON SOMETHING BEING TRUE OR FALSE


x = 20
y = 22


#SIMPLE IF
#if x > y:
    #print(x,"is greater than ",y)
    #print(f'{x} is greater than {y}')    #USED  FORMAT SPECIFIER F{} TO PRINT 

#IF AND ELSE
# if x > y:
#     #print(x,"is greater than ",y)
#     print(f'{x} is greater than {y}')    #USED  FORMAT SPECIFIER F{} TO PRINT 
# else:
#     print(f'{y} is greater than {x}') #USED


#   ELIF


# if x > y:
#     #print(x,"is greater than ",y)
#     print(f'{x} is greater than {y}')
# elif x == y:    
#     print(f'{x} is equal to {y}')    #USED  FORMAT SPECIFIER F{} TO PRINT    
# else:
#     print(f'{y} is greater than {x}') #USED


#    NESTED IF STATEMENT

# if x > 2:
#     if x <= 25:
#         print(f'{x} is greater than 2 and less than or equal to {x}')


#OPERATORS    AND   OR     NOT

#    AND
# if x > 2 and x <= 25:    #BOTH CONDITIONS NEEDS TO BE TRUE FOR AND OPERATOR TO RUN
#     print(f'{x} is greater than 2 and less than or equal to {x}')

#       OR 

# if x > 2 or x <= 27:  #one of the condition has to be TRUE
#     print(f'{x} is greater than 2 and less than or equal to {x}')



# #    NOT 
# if not( x == y ):
#     print(f'{x} is not equal to {y}')




#     MEMBERSHIP OPEARTORS --- test to see if something is in a list

numbers = [20,21,22,23,24,25,26,27,28,29,30]


# IN 
# if x in numbers:
#     print(x in numbers)


#   NOT IN 
# if x not in numbers:
#     print(x not in numbers)



#   identity operators  

#  is 
# if x is y:
#     print(x is y)

#   NOT

if x is not y:
    print(x is  not y)