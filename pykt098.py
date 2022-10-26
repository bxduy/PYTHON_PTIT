data = list()
with open('DATA.in') as f:
    lines = f.readlines()
    for line in lines:
        arr = line.split()
        for i in arr:
            try:
                n = int(i)
                if n >= 2**32:
                    data.append(i)
            except ValueError:
                data.append(i)
print(*sorted(data))