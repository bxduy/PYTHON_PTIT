import math
def check(n):
    if n < 2:
        return 0;
    if n == 2:
        return 1;
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
t = int(input())
while t > 0 :
    t = t-1
    a, b = [int(x) for x in input().split(" ")]
    n = int(math.gcd(a, b))
    tmp = 0
    while n > 0:
        tmp += n % 10;
        n //= 10
    if check(tmp):
        print("YES")
    else:
        print("NO")