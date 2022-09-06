n = int(input())
rev = 0
sq = n * n
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
sq1 = rev * rev
rev1 = 0
while sq1 > 0:
    rem1 = sq1 % 10
    rev1 = rev1 * 10 + rem1
    sq1 = sq1 // 10
if (rev1 == sq):
    print("True")
else:
    print("False")