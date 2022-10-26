t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    mapp = {}
    ls = [int(i) for i in input().split()]
    for i in ls:
        if i in mapp:
            mapp[i] = mapp.get(i) + 1
        else:
            mapp[i] = 1
    check = True
    for x in ls:
        if mapp[x] > n // 2:
            print(x)
            mapp[x] = 0
            check = False
    if check:
        print("NO")