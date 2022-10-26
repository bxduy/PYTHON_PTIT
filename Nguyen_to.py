import math


def check(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return 0
    return 1


t = int(input())
while t > 0:
    n = int(input())
    if check(n) == 1:
        print("YES")
    else:
        print("NO")
    t = t-1