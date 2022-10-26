t = int(input())
while t > 0:
    t-=1
    n, x, m = [float(i) for i in input().split(" ")]
    cnt = 0
    sum = n
    while sum < m:
        sum *= (1 + x/100)
        cnt += 1
    print(cnt)