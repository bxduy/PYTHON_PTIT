class Bill:
    def __init__(self, id, name, amount, price, dis):
        self.dis = dis
        self.price = price
        self.amount = amount
        self.name = name
        self.id = id
        self.total = self.amount*self.price-self.dis
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.amount, self.price, self.dis, self.total)
data = list()
for i in range(int(input())):
    data.append(Bill(input().strip(), input().strip(), int(input().strip()), int(input().strip()), int(input().strip())))
data = sorted(data, key=lambda x : -x.total)
for i in data:
    print(i)
# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000