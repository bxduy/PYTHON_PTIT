t = int(input())
while t > 0:
    t -= 1
    n = input()
    cnt = n.count("0") + n.count("1") + n.count("2")
    if cnt == len(n):
        print("YES")
    else:
        print("NO")