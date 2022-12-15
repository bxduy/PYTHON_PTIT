def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    a = sorted(a)
    print(len(a))
    lst = list()
    res = -1
    for i in range(0, n-1):
        if i <= res:
            continue
        tmp = list()
        tmp.append(a[i])
        for j in range(i+1, n):
            if a[j] - a[i] <= 1:
                tmp.append(a[j])
                res = j
        lst.append(tmp)
    sum = 0
    for i in lst:
        sum1 = 0
        for j in range():



t = int(input())
while t > 0:
    t -= 1
    solve()