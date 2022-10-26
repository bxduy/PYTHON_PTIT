t = int(input())
while t > 0:
    t -= 1
    s = input()
    cnt = 1
    ans = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans = ans + str(cnt) + s[i-1]
            cnt = 1
    ans += str(cnt) + s[len(s) - 1]
    print(ans)