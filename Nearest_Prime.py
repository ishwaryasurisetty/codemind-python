t = int(input())
for _ in range(t):
    n = int(input())
    nxt_prime = n
    while True:
        fc = 0
        for i in range(1, nxt_prime + 1):
            if nxt_prime % i == 0:
                fc += 1
        if fc == 2:
            break
        nxt_prime += 1
    pre_prime = n
    while True:
        fc = 0
        for i in range(1, pre_prime + 1):
            if pre_prime % i == 0:
                fc += 1
        if fc == 2:
            break
        pre_prime -= 1
    if n - pre_prime <= nxt_prime - n:
        print(pre_prime)
    else:
        print(nxt_prime)