ls = [1]
res = 1
for i in range(1, 10):
    res *= i
    ls.append(res)
t = int(input())
while t > 0:
    t -= 1
    n = input()
    ans = 0
    for i in n:
        i = int(i)
        ans += ls[i]
    n = int(n)
    if n == ans:
        print("YES")
    else:
        print("NO")