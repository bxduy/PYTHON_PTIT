import math


class Bill:
    def __init__(self, id, name, old, new):
        self.id = id
        self.name = name
        self.old = old
        self.new = new
        self.amount = self.new-self.old
    def cal(self):
        if self.amount <= 50:
            self.total = self.amount * 100 * 1.02
        elif self.amount <= 100:
            self.total = (50 * 100 + (self.amount - 50) * 150) * 1.03
        else:
            self.total = (50*100+50*150+(self.amount-100)*200)*1.05
    def __str__(self):
        if self.id < 10:
            return 'KH0{} {} {}'.format(self.id, self.name, math.ceil(self.total))
        else:
            return 'KH{} {} {}'.format(self.id, self.name, math.ceil(self.total))
data = list()
for i in range(int(input())):
    res = Bill(i+1, input(), int(input()), int(input()))
    res.cal()
    data.append(res)
data = sorted(data, key=lambda x : x.total, reverse=True)
for i in data:
    print(i)
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612
