def check(s, ss):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(ss[i]) - ord(ss[i-1])):
            return False
    return True
t = int(input())
while t > 0:
    t -= 1
    s = input()
    ss = s[::-1]
    if check(s, ss):
        print("YES")
    else:
        print("NO")
