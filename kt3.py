data = list()
for i in range(int(input())):
    s = input()
    data.append(s)
    if s == '':
        print(data[0] + ":", len(data)-2)
        data.clear()
print(data[0] + ":", len(data)-1)
