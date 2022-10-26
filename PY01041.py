def check(n):
    if len(n) < 3:
        return "NO"
    l = 0
    r = len(n) - 1
    while l < r:
        if n[l] < n[l+1]:
            l += 1
        elif n[r] < n[r-1]:
            r -= 1
        else:
            break
    if l == r:
        return "YES"
    else:
        return "NO"

t = int(input())
while t > 0:
     t -= 1
     n = input()
     print(check(n))