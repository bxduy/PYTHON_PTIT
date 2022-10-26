def check(s):
    if(s[len(s)-1] != '6' or s[len(s) - 2] != '8'):
        return False
    return True
t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
