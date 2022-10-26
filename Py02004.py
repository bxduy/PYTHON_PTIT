t = int(input())
cnt = 0
ls = [int(x) for x in input().split()]
for i in range(0, len(ls)-1):
    if ls[i] != ls[i+1]:
        cnt+=1

print(cnt)