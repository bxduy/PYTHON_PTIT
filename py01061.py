import math


def isPrime(num):
    for i in range(2, math.isqrt(num)):
        if num % i == 0:
            return False
    return num > 1
for i in range(int(input())):
    num = input()
    begin = int(num[:3])
    end = int(num[-3:])
    print("YES" if isPrime(begin) and isPrime(end) else "NO")