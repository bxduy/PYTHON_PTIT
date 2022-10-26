def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return num > 1
n = int(input())
a = [int(x) for x in input().strip().split()]
f = dict()
for i in a:
    if i in f:
        f[i] += 1
    else: f[i] = 1
for i in a:
    if isPrime(i) and f[i] > 0:
        print(i, f[i])
        f[i] = 0