import math


def check(n):
    if n == 2:
        return 1
    if n < 2:
        return 0;
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0;
    return 1;
t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt = cnt + 1
    if check(cnt):
        print("YES")
    else:
        print("NO")
    t = t-1