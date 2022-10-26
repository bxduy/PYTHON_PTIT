def solve():
    f = {}
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    check = False
    for i in a:
        if f[i] >= int(n/2)+1:
            check = True
            print(i)
            break
    if not check:
        print("NO")
for i in range(int(input())):
    solve()
