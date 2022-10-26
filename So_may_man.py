t = int(input())
for i in range(t):
    n = input()
    cnt = n.count("4") + n.count("7")
    if cnt == len(n):
        print("YES")
    else:
        print("NO")