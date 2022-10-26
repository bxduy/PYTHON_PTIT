n = int(input())
ls = [int(x) for x in input().split()]
cnt = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if ls[i] > ls[j]:
            cnt += 1
print(cnt)