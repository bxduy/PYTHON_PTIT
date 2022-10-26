test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    ls = input().split()
    ls2 = input().split()
    ls.sort()
    ls2.sort()
    check = True
    for i in range(0, n):
        if ls[i] > ls2[i]:
            check = False
    print("YES" if check else "NO")