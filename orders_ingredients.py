n = 5
ingre = "S S M M P"
p = 2
for i in range(p):
    order = "S S"

avail_ingred = ingre.split(" ")
orders = order.split(" ")
n = 0
for j in orders :
    if i in avail_ingred:
        avail_ingred.remove(i)
        n += 1
    else:
        print("NO")
        break

if n == len(orders):
    print("YES")
else:
    print("NO")