def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num > 1
n, m = map(int, input().split())
arr = list()
for i in range(n):
    arr.append([int(x) for x in input().split()])
for i in arr:
    for j in i:
        if isPrime(j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()