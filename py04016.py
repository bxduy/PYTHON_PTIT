import datetime


class Bill:
    def __init__(self, id, name, room, begin, end, bonus):
        self.end = end
        self.begin = begin
        self.room = room
        self.name = name
        self.id = 'KH%02d'%id
        self.bonus = bonus
        self.days = 0
        self.total = 0
    def tinhNgay(self):
        if self.begin == self.end: self.days = 1; return
        timein = datetime.datetime.strptime(self.begin, '%d/%m/%Y')
        timeout = datetime.datetime.strptime(self.end, '%d/%m/%Y')
        dist = str(timeout - timein)
        dist = [i for i in dist.split()]
        self.days = int(dist[0])+1
    def tinhTien(self):
        if self.room[0] == '1': self.total = self.days*25
        elif self.room[0] == '2': self.total = self.days*34
        elif self.room[0] == '3': self.total = self.days*50
        else: self.total = self.days*80
        self.total += self.bonus
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.room, self.days, self.total)
data = list()
for i in range(int(input())):
    name = input().strip()
    room = input().strip()
    begin = input().strip()
    end = input().strip()
    bonus = int(input().strip())
    id = i+1
    data.append(Bill(id, name, room, begin, end, bonus))
for i in data:
    i.tinhNgay()
    i.tinhTien()
data = sorted(data, key=lambda x : -x.total)
for i in data:
    print(i)
# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96
