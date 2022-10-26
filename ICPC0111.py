t = int(input())
while t > 0:
    t -= 1
    n, k = [int(x) for x in input().split(" ")]
    ls = [int(ls) for ls in input().split(" ")]
    for i in range(k, n):
        print(ls[i], end=" ")
    for i in range(0, k):
        print(ls[i], end=" ")
    print()

