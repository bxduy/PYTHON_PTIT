def c(n, k):
    if k == n or k == 0:
        return 1
    return c(n-1, k) + c(n-1, k-1)
n = int(input())
ls = []
for i in range(0, n):
    s = input()
    tmp = []
    for x in s:
        tmp.append(x)
    ls.append(tmp)
ans = 0
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if ls[i][j] == 'C':
            cnt += 1
    if cnt >= 2:
        ans += c(cnt, 2)
for j in range(0, n):
    cnt = 0
    for i in range(0, n):
        if ls[i][j] == 'C':
            cnt += 1
    if cnt >= 2:
        ans += c(cnt, 2)
print(ans)
