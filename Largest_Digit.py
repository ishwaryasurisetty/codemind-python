n = int(input())
large = 0
while n > 0:
    rem = n%10
    if large < rem:
        large = rem
    n = n // 10
print(large)