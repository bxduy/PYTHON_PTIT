def check(s):
    tmp = s[::-1]
    return s == tmp
map = dict()
listString = list()
with open('VANBAN.in') as f:
    lines = f.readlines()
    for line in lines:
        arr = line.split()
        for i in arr:
            if check(i):
                if i in map:
                    map[i] = map[i]+1
                else:
                    map[i] = 1
                    listString.append(i)
listString = sorted(listString, key=lambda x : -len(x))
res = 0
for i in listString:
    if len(i) >= res:
        res = len(i)
        print(i, map[i], sep=" ")
    else:
        break