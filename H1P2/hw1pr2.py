# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name: 
# Problem description: Solving the quadratic equation!

from math import *

#x = input("Supply a number: ")
#x = float(x)
#print("The value stored by the variable x is",x)
a = float(input("Supply a number for a: "))
b = float(input("Supply a number for b: "))
c = float(input("Supply a number for c: "))
PartOne = (b**2 -4 * a * c)
PartTwo = sqrt(PartOne)
Pos = (-(b) + PartTwo) / (2 * a)
Neg = (-(b) - PartTwo) / (2 * a)
print("The solutions for x are: ", Pos, "and", Neg)