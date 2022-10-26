import math


def isPrime(n):
    n = int(n)
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
     t -= 1
     n = input()
     sum = 0
     for i in range(1, 10):
         sum += n.count(str(i)) * i
     print("YES" if isPrime(sum) else "NO")