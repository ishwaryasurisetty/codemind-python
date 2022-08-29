import math
n = int(input())
for i in range(1, n+1):
    a = int(input())
    b = int(math.sqrt(a))
    if (a == b * b):
        print("True")
    else:
        print("False")