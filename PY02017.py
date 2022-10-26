t = int(input())
while t > 0:
     t -= 1
     n = int(input())
     arr = [int(i) for i in input().split()]
     ans = arr[0]
     for i in range(1, n):
         ans ^= arr[i]
     print(ans)