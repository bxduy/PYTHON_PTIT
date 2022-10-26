class Submit:
    def __init__(self, name, ac, sub):
        self.name = name
        self.ac = ac
        self.sub = sub
    def __str__(self):
        return self.name + " " + str(self.ac) + " " + str(self.sub)
data = list()
for i in range(int(input())):
    name = input()
    ac, sub = map(int, input().split())
    data.append(Submit(name, ac, sub))
data = sorted(data, key=lambda x : (-x.ac, x.sub, x.name))
for i in data:
    print(i)
# 4
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 168 600
# Bui Xuan Duy
# 170 500
# Do Minh Ngoc
# 170 450
