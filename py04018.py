class Teacher:
    def __init__(self, idT, id, name, p1, p2):
        self.sta = ""
        self.total = 0
        self.pri = 0
        self.sub = ""
        self.p2 = p2
        self.p1 = p1*2
        self.name = name
        self.id = 'GV%02d'%id
        self.idT = idT
    def uutien(self):
        if self.idT[1] == '1': self.pri = 2
        elif self.idT[1] == '2': self.pri = 1.5
        elif self.idT[1] == '3': self.pri = 1
        else: self.pri = 0
    def xh(self):
        self.total = self.p1 + self.p2 + self.pri
        if self.total >= 18: self.sta = "TRUNG TUYEN"
        else: self.sta = "LOAI"
    def mon(self):
        if self.idT[0] == 'A': self.sub = "TOAN"
        elif self.idT[0] == 'B': self.sub = "LY"
        else: self.sub = "HOA"
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.sub, '%.1f'%self.total, self.sta)
data = list()
for i in range(int(input())):
    id = i+1
    name = input().strip()
    idT = input().strip()
    p1 = float(input().strip())
    p2 = float(input().strip())
    data.append(Teacher(idT, id, name, p1, p2))
for i in data:
    i.uutien()
    i.xh()
    i.mon()
data = sorted(data, key=lambda x : -x.total)
for i in data:
    print(i)
# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0
