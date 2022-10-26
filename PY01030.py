import math

n, k = [int(x) for x in input().split()]
cnt = 0
for i in range(pow(10, k-1), pow(10, k)):
    if math.gcd(i, n) == 1:
        print(i, end=" ")
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0