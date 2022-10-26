t = int(input())
while t > 0:
     t -= 1
     n = int(input())
     a = [int(a) for a in input().split()]
     cnt = 0
     for i in range(0, n):
         for j in range(i+1, n):
             for k in range(j+1, n):
                 if a[i] + a[j] + a[k] == 0:
                     cnt += 1
     print(cnt)