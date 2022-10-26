import datetime
data1 = list()
data2 = list()
class TL:
    def __init__(self, id, name):
        self.id = 'TL%03d'%id
        self.name = name
class Rap:
    def __init__(self, id, room, time, name, amount):
        self.id = id
        self.room = 'P%03d'%room
        self.time = time
        self.name = name
        self.amount = amount
        self.tl = ""
        self.timeP = datetime.datetime.strptime(self.time, '%d/%m/%Y')
    def __str__(self):
        return '{} {} {} {} {}'.format(self.room, self.tl, self.time, self.name, self.amount)
def xdtl(tL: TL, rap:Rap):
    rap.tl = tL.name
n, m = map(int, input().split())
for i in range(n):
    data1.append(TL(i+1, input().strip()))
for i in range(m):
    data2.append(Rap(input().strip(), i+1, input().strip(), input().strip(), int(input().strip())))
for i in data1:
    for j in data2:
        if i.id == j.id:
            xdtl(i, j)
data2 = sorted(data2, key= lambda x : (x.timeP, x.name, -x.amount))
for i in data2:
    print(i)
# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5
