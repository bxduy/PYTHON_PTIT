class TTLM:
    def __init__(self, name, time, amount, id):
        self.name = name
        self.time = time
        self.id = id
        self.amount = amount
        self.tb = round(self.amount/self.time*60, 2)
def tinhtg(begin, end):
    timebg = [int(x) for x in begin.split(":")]
    timeed = [int(x) for x in end.split(":")]
    return timeed[0]*60+timeed[1] - timebg[0]*60-timebg[1]
def xdid(n):
    if len(str(n)) < 2:
        return "T0" + str(n)
    else:
        return "T" + str(n)
lst = []
lstten = []
for i in range(int(input())):
    id = xdid(i+1)
    name = input()
    begin = input()
    end = input()
    amount = int(input())
    time = tinhtg(begin, end)
    if name not in lstten:
        lstten.append(name)
        lst.append(TTLM(name, time, amount, id))
    else:
        for j in lst:
            if name == j.name:
                time += j.time
                amount += j.amount
                id = j.id
                lst.remove(j)
                lst.append(TTLM(name, time, amount, id))
                break
lst = sorted(lst, key=lambda i : i.id)
for i in lst:
    print('{} {} {}'.format(i.id, i.name, '%.2f'%i.tb))
# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35