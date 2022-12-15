from itertools import permutations

t = int(input())
while t > 0:
    n = int(input())
    arr = [i for i in range(1, n+1, 1)]
    perm = permutations(arr, n)
    a = []
    for i in perm:
        s=""
        for j in i:
            s+=str(j)
        a.append(s)
    a.sort(reverse= True)
    print(len(a))
    for i in a:
        print(i, end = " ")
    print()
    t-=1