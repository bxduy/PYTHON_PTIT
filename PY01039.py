t = int(input())
while t > 0:
    t -= 1
    n = input()
    s = set()
    check = True
    for i in range(len(n) - 2):
        s.add(int(n[i]))
        s.add(int(n[i+2]))
        if len(s) > 2 or n[i] != n[i+2]:
            check = False
            break
    if len(s) < 2:
        check = False
    if check:
        print("YES")
    else:
        print("NO")