#!/usr/bin/python3.5

# import fileinput
import sys

print("process stdin")
print("sys.version.info")

# i = 0
# for line in fileinput.input() :
# 
#   if i > 5 : break
#   print(i, line, end="")
#   i += 1

things = (5, 4, 3, 2, 1)

# Preincrement doesn't do anything
i = 0
print(things[++i])
print(things[i+1])

binary = sys.stdin.read(42)
print("read size", len(binary))
