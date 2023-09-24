# Python syntax is indentation heavy
print("Hello World!")

# This is a sample comment

#---- VARIABLES & DATA TYPES ----#
# Variable (in programming) - is a placeholder for data
# Value - this is the data assigned to a variable
# Data types - the kind of data assigned to a variable (ex. strings, integers, floats, etc.)
# !! In Python, you do not assign data types, because Python is a "dynamically-typed programming languauge"

a = "Hello" # this is a string
b = "5" # this is an int

# print(a+b) # "Hello5"
a = 5 # this is an integer
# print(a+int(b)) # 10 (have to turn variable b into an int type before adding)

#---- INPUT & OUTPUT ----#
# input() - take input from the user
# age = input("Type in your age: ") #--> input smth from user
# print(age,"yrs. old") #--> print or output smth to the user

#---- ARITHMETHIC OPERATIONS ----#
a = 10 #int
b = 5 #int

print(a+b) #addition
print(a-b) #subtraction 
print(a*b) #multiplication
print(a/b) #float division
print(a//b) #integer division
print(a**b) #exponentiation

#---- COMPARISON OPERATIONS ----#
c = 12
d = 4
e = "4"

print(c>d) # True
print(c<d) # False
print(c>=d) # True
print(c<=d) # False
print(c==d) # False
print(d==e) # False

#---- LOGICAL/BOOLEAN OPERATORS ----#
# input are boolean values

print("boolean operators:")

t = True
f = False

print(t and f)
print(t or f)
print(not t)
print(not f)
print(t ^ t) # XOR (^)
