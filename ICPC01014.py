import math

prime = []
nonPrime = [0, 1]
def erathone():
    for i in range(2, 1000001):
        if not i in nonPrime:
            prime.append(i)
            for j in range(i*i, 1000001, i):
                if not j in nonPrime:
                    nonPrime.append(j)

def check(num):
    if not int(num) in prime:
        return False
    if not int(num[::-1]) in prime:
        return False
    sum = 0
    for i in num:
        if not int(i) in prime:
            return False
        sum += int(i)
    if not sum in prime:
        return False
    return True


erathone()
t = int(input())
while t > 0:
     t -= 1
     num = input()
     print("Yes" if check(num) else "No")


