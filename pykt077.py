import datetime


class Mon:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Thi:
    def __init__(self, id, timed, timeh, gr, stt):
        self.stt = 'T%03d'%stt
        self.id = id
        self.timed = timed
        self.gr = gr
        self.timeh = timeh
        self.timeD = datetime.datetime.strptime(self.timed, '%d/%m/%Y')
        self.timeH = datetime.datetime.strptime(self.timeh, '%H:%M')
        self.name = ""
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.stt, self.id, self.name, self.timed, self.timeh, self.gr)
def getName(mon:Mon, thi:Thi):
    thi.name = mon.name
n, m = map(int, input().split())
listm = list()
listt = list()
for i in range(n):
    listm.append(Mon(input().strip(), input().strip()))
for i in range(m):
    a = [i for i in input().strip().split()]
    stt = i+1
    listt.append(Thi(a[0], a[1], a[2], a[3], stt))
for i in listm:
    for j in listt:
        if i.id == j.id:
            getName(i, j)
listt = sorted(listt, key=lambda x : (x.timeD, x.timeH, x.id))
for i in listt:
    print(i)
# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05