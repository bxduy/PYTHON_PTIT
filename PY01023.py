import math


def phan_tich(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            print("* "  + str(i) + "^" + str(cnt) , end=" ")
    if n != 1:
        print("* " + str(n) + "^1" , end="")
t = int(input())
while t > 0:
    n = int(input())
    print("1", end=" ")
    phan_tich(n)
    print()