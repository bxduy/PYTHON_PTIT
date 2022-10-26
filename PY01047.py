import math


def isPrime(n):
    n = int(n)
    if n < 2 or n % 2 == 0:
        return False
    if n == 2:
        return True
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n = input()
    n = n[max(0, len(n)-4):]
    print("YES" if isPrime(n) else "NO")
