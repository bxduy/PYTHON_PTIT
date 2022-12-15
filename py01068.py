from itertools import combinations

n, m = map(int, input().split())
arr = input().split()
res = set(arr)
sett = sorted(res)
for i in list(combinations(sett, m)):
    for j in i:
        print(j, end=" ")
    print()