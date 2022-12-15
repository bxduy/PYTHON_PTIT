class Subject:
    def __init__(self, id, name, form):
        self.id = id
        self.name = name
        self.form = form
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.form)
data = list()
for i in range(int(input())):
    data.append(Subject(input(), input(), input()))
data = sorted(data, key=lambda x : x.id)
for i in data:
    print(i)
# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen