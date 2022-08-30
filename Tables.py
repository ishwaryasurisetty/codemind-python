n, r = map(int,input().split())
for i in range(1, r+1, 2):
    num = n * i
    print(n, 'x', i, '=', num)