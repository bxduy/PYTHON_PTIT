import datetime


class Athlete:
    def __init__(self, name, add, end):
        self.name = name
        self.add = add
        self.end = end
        self.id = ""
        self.hours = 0
        self.speed = 0
    def createID(self):
        ten = self.name.split()
        dc = self.add.split()
        ans = ""
        for i in dc: ans += i[0]
        for i in ten: ans += i[0]
        self.id = ans
    def cal(self):
        begin = datetime.datetime.strptime("6:00","%H:%M")
        end = datetime.datetime.strptime(self.end,"%H:%M")
        tmp = end - begin
        self.hours = tmp.seconds/3600
        self.speed = 120/self.hours
    def __str__(self):
        return self.id + " " + self.name + " " + self.add + " " + str(round(self.speed)) +" Km/h"
data = list()
for i in range(int(input())):
    tmp = Athlete(input(), input(), input())
    tmp.createID()
    tmp.cal()
    data.append(tmp)
data = sorted(data, key=lambda x : x.speed, reverse=True)
for i in data:
    print(i)
# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45