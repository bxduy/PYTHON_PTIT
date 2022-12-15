def solve(a, n):
    cnt = 100000000
    for i in range(n):
        tmp = 0
        check = True
        for j in range(n):
            res = (a[i] - abs(i - j))
            if res > 0:
                tmp += abs(a[j] - res)
            else:
                check = False
                break
        if check:
            cnt = min(cnt, tmp)
    return cnt


n = int(input())
a = [int(i) for i in input().split()]
cnt = solve(a, n)
print(cnt)
