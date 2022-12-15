import math

n = int(input())

data = [int(i) for i in input().split()]
data = sorted(data)
for i in range(n-1):
    for j in range(i+1, n):
        if math.gcd(data[i], data[j]) == 1:
            print(data[i], data[j])