prime = []
nonPrime = [0, 1]

def erathone():
    for i in range(2, 10000):
        if not i in nonPrime:
            prime.append(i)
            for j in range(i*i, 10000, i):
                 if not j in nonPrime:
                     nonPrime.append(j)

erathone()
n, x = [int(x) for x in input().split()]
print(x, end = " ")
for i in range(0, n):
    x += prime[i]
    print(x, end = " ")