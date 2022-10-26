def solve(ls, index):
    cnt = 0
    for i in range(0, len(ls)):
        if i != index:
            tmp = ls[i]
            while(tmp != ls[index]):
                cnt += 1
                tmp = tmp[1:] + tmp[0]
                if tmp == ls[i]:
                    return -1
    return cnt
t = int(input())
ls = []
ans = 100000
for i in range(0, t):
    ls.append(input())
check = True
for i in range(0, len(ls)):
    res = solve(ls, i)
    if res == -1:
        print(res)
        check = False
        break
    else:
        ans = min(ans, res)
if check:
    print(ans)


