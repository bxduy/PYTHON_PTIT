import math

n = int(input())
ls = [int(x) for x in input().split()]
ls.sort()
for i in range(0, n-1):
    for j in range(i+1, n):
        if math.gcd(ls[i], ls[j]) == 1:
            print(ls[i], ls[j], sep = " ")