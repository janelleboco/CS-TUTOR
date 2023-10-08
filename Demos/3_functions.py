# FUNCTIONS
# way making of making your code modular
# modular = the stuff written inside here can be used again and again

# PARTS OF A FUNCTION
# name
# input / parameter
# output / return statement

# def print_name(name):
#     print("Hello,",name)

# username = input()
# print_name(username)

# square the input number
# def magic(n):
#     return n * n     

# for i in range(10):
#     a = magic(i)
#     print(a)

# function with multiple parameters - order matters
# you can have NAMED PARAMETERS

def add(a,b):
    print('a = ',a)
    print('b = ',b)
    return a + b

print(add(b=1,a=2))


# SCOPING
# your variables are only accessible by certain parts of the code

x = 1 #this is a global variable (it can be used anywhere)

def function():
    a = 5 #this is a local variable (it can only be used within the function)
    b = 10
    c = 20
    return a

# you can pass a lot of things as parameters
def lol():
    print("hello world")

def wow(thing):
    thing()
    # print(thing)

wow(lol)
