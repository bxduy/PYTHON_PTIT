t = int(input())
while t > 0:
     t -= 1
     n = input()
     sum = 0
     for i in range(1, 10):
         sum += n.count(str(i)) * i
     if sum >= 10 and str(sum) == str(sum)[::-1]:
         print("YES")
     else:
         print("NO")
