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
    cnt = n.count("2") + n.count("3") + n.count("5") + n.count("7")
    m = len(n)
    m//=2
    if isPrime(len(n)) and cnt > m:
        print("YES")
    else:
        print("NO")

