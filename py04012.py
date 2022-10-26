class Student:
    def __init__(self, id, name, cl):
        self.cl = cl
        self.name = name
        self.id = id
        self.point = 10
        self.sta = ""
    def attendance(self, s):
        for i in s:
            if i == 'v': self.point -= 2
            elif i == 'm': self.point -= 1
        if self.point <= 0: self.point = 0
    def evaluate(self):
        if self.point != 0:
            self.sta = ""
        else: self.sta = "KDDK"
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.cl, self.point, self.sta)
n = int(input())
data = list()
for i in range(n):
    data.append(Student(input().strip(), input().strip(), input().strip()))
for i in range(n):
    s = input()
    res = [i for i in s.split()]
    for i in data:
        if res[0] == i.id: i.attendance(res[1])
for i in data:
    i.evaluate()
    print(i)
# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm