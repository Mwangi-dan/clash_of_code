"""
The game mode is REVERSE

Finding out what to do with only the output
"""
import sys
import math

x = ()
n = int(input("Num: "))
for i in range(n):
    student = input("Student: ")
    score = int(input("Score: "))
    x = x + ((student, score),)
x = sorted(x, key=lambda x: x[1])
for i in range(n):
    print(f"{i+1}, {x[n-i-1][0]}, {x[n-i-1][1]}")

