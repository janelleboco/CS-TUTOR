#---- CONTROL STRUCTURES ----#
# This dictate the flow of your program

#-- CONDITIONALS --#
# if-else statements
# password_reference = "hello@world"
# password_input = input("Type in your password:")

# if password_input == password_reference: #if-block
#     print("You're logged in.")
# else: #else-block
#     print("Wrong password. Please try again.")

# elif statements
# grade = int(input("Type in your subject grade: "))

# if grade >= 90:
#     print("Good Pass!")
# elif grade >= 80:
#     print("Ok Pass hehe")
# elif grade >= 60:
#     print("Pasado parin")
# else:
#     print("You failed!")

# nesting + complicated conditionals
# a = True
# b = False

# if a and b:
#     print("hello")
# else:
#     print("world")

#-- LOOPS --#
# print 1-100 in the terminal

# while loop - just check if condition is true, then do something
# a = 1
# while a <= 100:
#     print(a)
#     a += 1 #--> IMPORTANT! UPDATE THE CONDITION

# for loop - iterate over something
# SYNTAX: range(start, end, step)
# for i in range(1,101,1):
#     print(i)

# DEFAULT range(0 SYNTAX:
# default start = 0
# end = N/A --> you need to define this
# default step = 1
for i in range(100): #0-indexed counting
    print(i+1)

# i = 0, print 1
# i = 1, print 2
# i = 2, print 3
# ...
# i = 99, print 100
# i = 100, STOP

