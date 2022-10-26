class Members:
    def __init__(self, idM, name, idT):
        self.idM = 'C%03d'%idM
        self.name = name
        self.idT = idT
    def __str__(self):
        return '{} {}'.format(self.idM, self.name)

class Teams:
    def __init__(self, idT, nameT, nameU):
        self.idT = 'Team%02d'%idT
        self.nameT = nameT
        self.nameU = nameU
    def __str__(self):
        return '{} {}'.format(self.nameT, self.nameU)

n = int(input())
dataT = list()
dataM = list()
for i in range(n):
    dataT.append(Teams(i+1, input().strip(), input().strip()))
m = int(input())
for i in range(m):
    dataM.append(Members(i+1, input().strip(), input().strip()))
dataM = sorted(dataM, key=lambda x : x.name)
for i in dataM:
    print(i, end=" ")
    for j in dataT:
        if j.idT == i.idT:
            print(j)
# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02
