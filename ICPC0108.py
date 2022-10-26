t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    a.sort()
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if a[left] + a[right] == -a[i]:
                cnt += 1
                print(f"{a[i]} {a[left]} {a[right]}")
                left += 1
                right -= 1
            elif a[left] + a[right] < -a[i]:
                left += 1
            else:
                right -= 1
    print(cnt)
