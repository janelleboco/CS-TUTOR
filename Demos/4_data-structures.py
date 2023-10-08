# Lists - collection of things (array or vector)
b = [5, 10, 30] #index: 0 1 2 ...
c = ["apple", "banana", "chocolate"]
a = [10, 'c', 'words', [5, 10, 20]] #mix data types are allowed
matrix2D = [                   #this is a 2d matrix represented as a list
    [10, 20, 30],
    [10, 20, 30],
    [10, 20, 30],
    ]

# print(matrix2D[0][0])

# lists are iterable - you can go over the elements
# for i in a:
#     print(i)

# # lists are dynamic - you can add or remove elements
# a.append(21903912093)
# for i in a:
#     print(i)
# a.pop(4)
# for i in a:
#     print(i)

# Dictionaries
# associated list 
# a unique key (your word in your dictionary, aka. the label) - value (associated thing to that word)
# ages = {
#     15 : "janelle",
#     17 : "davis",
#     21 : "karlo",
# }
# print(ages[21]) #superscript notation
# ages[21] = "jose"
# print(ages[21])

# Tuples
# pairs/tuples of values
# advantage: it's a good visualization of pairs
# t1 = (10, 20)
# print(t1[0],t1[1])

# Sets - secure structure
# Immutable tuple | unordered, unchangeable, unindexable | distinct elements
s1 = set()
s1.add(10)
s1.add(20)
s1.add(10)
# print(s1)

#access is only through iteration
for i in s1:
    print(i)

