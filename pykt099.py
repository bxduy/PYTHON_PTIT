with open('DATA1.in') as file_object:
    lines = file_object.readlines()
set1 = set()
set2 = set()
for line in lines:
    a = [i for i in line.strip().lower().split()]
    for j in a:
        set1.add(j)
with open('DATA2.in') as file_object:
    lines = file_object.readlines()
for line in lines:
    a = [i for i in line.strip().lower().split()]
    for j in a:
        set2.add(j)
set3 = set1.difference(set2)
set4 = set2.difference(set1)
set3 = sorted(set3)
set4 = sorted(set4)
for i in set3:
    print(i, end=" ")
print()
for i in set4:
    print(i, end=" ")