cnt = 0
def Try(i, s1, s2, sum, a, n):
    global cnt
    if s1 > sum // 3 or s2 > sum // 3:
        return
    if sum - s1 - s2 == sum // 3:
        cnt += 1
        return
    for j in range(i+1, n):
        Try(j, s1 + a[j], s2, sum, a, n)
        Try(j, s1, s2 + a[j], sum, a, n)
for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for j in a:
        sum += j
    if sum % 3 != 0:
        print(0)
        continue
    Try(-1, 0, 0, sum, a, n)
    print(cnt)
    cnt = 0