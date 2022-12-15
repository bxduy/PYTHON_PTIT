def check(num):
    s = str(num)
    sum = 1
    for i in s:
        sum *= int(i)
    return sum
def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (check(a[j]) < check(a[i])) or (check(a[j]) == check(a[i]) and a[j] < a[i]):
                a[i], a[j] = a[j], a[i]
    for i in a:
        print(i, end=" ")
t = int(input())
for i in range(t):
    solve()
    print()
# 1
# 8
# 143 43 22 99 7 9 1111 10000000