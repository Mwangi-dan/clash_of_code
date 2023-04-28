"""
f(x) = a * x + b

"""

a, b = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    x = int(input())
    sol = (a * x + b)
    print(sol)