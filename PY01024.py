def check(s):
    tmp = int(s[0])
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            return False
        tmp += int(s[i])
    return tmp % 10 == 0
t = int(input())
while t > 0:
     t -= 1
     s = input()
     if check(s):
         print("YES")
     else:
         print("NO")