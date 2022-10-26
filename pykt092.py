class ThiSinh:
    def __init__(self, name, point, ethnic, area, id):
        self.id = 'TS%02d'%id
        self.name = name
        self.point = point
        self.ethnic = ethnic
        self.area = area
        self.pri = 0
        self.total = 0
        self.sta = ""
    def getPri(self):
        if self.area == '1': self.pri = 1.5
        elif self.area == '2': self.pri = 1
        else: self.pri = 0
        if self.ethnic == 'Kinh': self.pri += 0
        else: self.pri += 1.5
    def getTotal(self):
        self.total = self.pri + self.point
        if self.total >= 20.5: self.sta = "Do"
        else: self.sta = "Truot"
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.total, self.sta)
data = list()
for i in range(int(input())):
    res = [i.capitalize() for i in input().split()]
    name = ""
    for j in res:
        name += j + " "
    id = i+1
    data.append(ThiSinh(name.strip(), float(input().strip()), input().strip(), input().strip(), id))
for i in data:
    i.getPri()
    i.getTotal()
data = sorted(data, key=lambda x : (-x.total, x.id))
for i in data:
    print(i)
# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3