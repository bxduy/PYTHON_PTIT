ls = []
ls.append(0)
ls.append(1)
ls.append(1)
for i in range(3, 94):
    ls.append(ls[i-2] + ls[i-1])
t = int(input())
while t > 0:
    t -= 1
    n, k = [int(i) for i in input().split(" ")]
    for i in range(n, k+1):
        print(ls[i], end=" ")
    print()
