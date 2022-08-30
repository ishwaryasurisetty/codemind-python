n = int(input())
sum = 0
sq = n * n
while sq > 0:
    rem = sq % 10
    sum += rem
    sq = sq // 10
if (n == sum):
    print("Neon Number")
else:
    print("Not Neon Number")