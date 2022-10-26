a, k, n = [int (x) for x in input().split(" ")]
check = 1
tmp = k-a
while tmp <= 0:
    tmp += k
for i in range(tmp, n-a+1, k):
    if (a+i) % k == 0:
        print(i, end=" ")
        check = 0
if check :
    print(-1)

