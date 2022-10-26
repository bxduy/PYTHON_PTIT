t = int(input())
while t > 0 :
    t -= 1
    s = input()
    tmp = ""
    ans = 1e20
    for i in range(0, len(s)):
        if s[i].isdigit():
            tmp += s[i]
        else:
            if len(tmp) != 0:
                tmp = int(tmp)
                ans = min(ans, tmp)
            tmp = ""
    if len(tmp) != 0:
        tmp = int(tmp)
        ans = min(ans, tmp)
    print(ans)