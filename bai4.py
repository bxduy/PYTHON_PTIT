n = int(input())
mapp = {}
ans = []
while n > 0:
    n -= 1
    s = input().lower()
    ls = s.split()
    res = []
    for x in ls:
        tmp = ""
        for i in x:
            if i.isalpha() or i.isdigit():
                tmp += i
            else:
                if tmp != "":
                    res.append(tmp)
                tmp =""
        if tmp != "":
            res.append(tmp)
    for x in res:
        ans.append(x)
ans.sort()
for x in ans:
    if x in mapp:
        mapp[x] = mapp.get(x) + 1
    else:
        mapp[x] = 1
result = sorted(mapp.items(), key = lambda x : x[1], reverse = True)
for x in result:
    print(x[0], x[1], sep = " ")
