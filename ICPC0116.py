t = int(input())
while t > 0:
     t -= 1
     s = input()
     if s[len(s) - 1] == s[0]:
         print("YES")
     else:
         print("NO")