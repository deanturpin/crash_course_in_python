#!/usr/bin/python3.5

# import random
# import sys
# import os

# I am a single line comment

'''
I am a multi-line
comment
'''

print ("Hello")

# Declare a variable
name = "Ken"

print(name)

'''
Types
- Numbers
- Strings
- Lists
- Tuples
- Dictionaries (maps)
'''

# Arithmetic operators
# + - *  / % ** //

name = 15

print("blah", 17, "yah", 4//3)

# Strings
quote1 = "\"always remember\'"
quote2 = '"always remember"'
quote3 = '''this is
   a multi-line quote'''
quote4 = quote1 + quote2

print(quote1)
print(quote2)
print(quote3)
print(quote4)

print("%s %s %s" % (quote1, quote2, quote3)) 

print("don't print a newline", end="")
print("newline again")
print("5" * 5, 4 * 4, 5 + 4)

# Lists
animals = ["goat", "cat", "squirrel"]
print(animals[0:3])
plants = ["tree", "basil"]

things = [animals, plants]
print(things)
print(things[1][1])
things[1].append("badger")
print(things)

things[1].remove("tree")
things[1].sort()
things[0:1].sort()
things.sort()
print(things)
things[1].sort()
things[1].reverse()
del things[0][0]
print(things)

flat_list = things[0] + things[1]
print(flat_list)
print("flat list contains", len(flat_list))
print("max", max(flat_list))
print("min", min(flat_list))

# Tuples - can't change tuples

pi_tuple = (3,1,4,1,4,9)
pi_list = list(pi_tuple)
print(pi_tuple)
# pi_tuple[0] = 1 # No!
print(pi_list)

# Convert between
print(list(pi_tuple))
print(tuple(pi_list))
print(len(pi_tuple))
print(min(pi_tuple))
print(max(pi_tuple))

# Dictionaries (or maps)
# Similar to lists but can't concatenate with +

supper_villains = {"Ken" : 0, "Gary" : 1}
supper_villains["Ken"] = 1
print(supper_villains["Gary"])
print(supper_villains.get("Gary"))
print(len(supper_villains))

keys = supper_villains.keys()
print(keys)

values = supper_villains.values()
print(max(values))

# Conditionals
age = 19

if age > 16 :
  print("You are old enough to drive")
else : # elif
  print("You are NOT old enough to drive")

# Logical operators
if age >= 1 and age < 18 :
  print("1-18")
elif not age > 20 :
  print("blah")

# Loops
for x in range(0, 10) : print(x, end=" "); print("hello")
for x in things : print(x)
for x in (1,2,3,4) : print(x, end=",\n")
for x in range(1,4) : print(x, end=",\n")
