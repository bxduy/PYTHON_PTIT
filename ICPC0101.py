n = int(input())
ls = []
a = [int(a) for a in input().split(" ")]
for i in a:
    if len(ls) == 0 or (ls[len(ls) - 1] + i) % 2 != 0:
        ls.append(i)
    else:
        ls.pop()
print(len(ls))