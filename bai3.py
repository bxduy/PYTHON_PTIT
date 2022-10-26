t = int(input())
while t > 0:
     t -= 1
     ls = []
     mapp = {}
     n = int(input())
     for i in range(0, n):
         tmp = int(input())
         ls.append(tmp)
         if tmp in mapp:
             mapp[tmp] = mapp.get(tmp) + 1
         else:
             mapp[tmp] = 1
     m = -1
     for x in mapp:
         m = max(m, mapp.get(x))
     ls.sort()
     for x in ls:
         if mapp[x] == m:
             print(x)
             break