import datetime


class MonThi:
    def __init__(self, idSub, nameSub, form):
        self.idSub = idSub
        self.nameSub = nameSub
        self.form = form
    def __str__(self):
        return '{}'.format(self.nameSub)


class CaThi:
    def __init__(self, i, date, hour, idR):
        self.date = date
        self.hour = hour
        self.idR = idR
        self.TimeD = datetime.datetime.strptime(self.date, '%d/%m/%Y')
        self.TimeH = datetime.datetime.strptime(self.hour, '%H:%M')
        self.idE = 'C%03d'%i
    def __str__(self):
        return '{} {} {}'.format(self.date, self.hour, self.idR)



class LichThi:
    def __init__(self, idE, idSub, idGr, amount):
        self.idE = idE
        self.idSub = idSub
        self.idGr = idGr
        self.amount = amount
    def __str__(self):
        return '{} {}'.format(self.idGr, self.amount)

listCa = list()
listMon = list()
listLich = list()
with open('MONTHI.in') as f:
    lines = f.readlines()
for i in range(1, int(lines[0])*3+1, 3):
    listMon.append(MonThi(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()))

with open('CATHI.in') as f:
    lines = f.readlines()
j = 1
for i in range(1, int(lines[0])*3+1, 3):
    listCa.append(CaThi(j, lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()))
    j += 1

with open('LICHTHI.in') as f:
    lines = f.readlines()
for i in range(1, int(lines[0])+1):
    a = lines[i].split()
    listLich.append(LichThi(a[0], a[1], a[2], a[3]))
listCa = sorted(listCa, key=lambda x : (x.TimeD, x.TimeH, x.idE))

for i in listCa:
    print(i, end=" ")
    for j in listLich:
        if j.idE == i.idE:
            for k in listMon:
                if j.idSub == k.idSub:
                    print(k, j)