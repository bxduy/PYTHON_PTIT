set1 = set()
set2 = set()
s = [x for x in input().lower().split()]
for i in s:
    set1.add(i)
s = [x for x in input().lower().split()]
for i in s:
    set2.add(i)
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set3 = sorted(set3)
set4 = sorted(set4)
for i in set3:
    print(i, end=" ")
print()
for i in set4:
    print(i, end=" ")