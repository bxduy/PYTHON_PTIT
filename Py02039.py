ls = []
n = int(input())
for i in range(0, n):
    tmp = [int(x) for x in input().split()]
    ls.append(tmp)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(0, n):
    for j in range(0, n):
        if j < n-i-1:
            sum1 += ls[i][j]
        elif j != n-i-1:
            sum2 += ls[i][j]
print("YES" if (abs(sum1-sum2) <= k) else "NO")
print(abs(sum1-sum2))