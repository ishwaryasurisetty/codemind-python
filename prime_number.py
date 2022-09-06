n = int(input())
cnt = 0
i = 1
while n >= i:
    if n%i == 0:
        cnt += 1
    i +=  1
if (cnt == 2):
    print("prime")
else:
    print("not a prime")
    