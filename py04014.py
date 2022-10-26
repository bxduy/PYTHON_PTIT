class Student:
    def __init__(self, name, point, id):
        self.name= name
        self.point = point
        self.id = id
        self.rating = ""
        self.average = 0
    def tb(self):
        sum = cnt = 0
        for i in self.point:
            if cnt <= 1:
                sum += i*2
            else:
                sum += i
            cnt += 1
        self.average = round(sum/10/1.2, 1)
    def xh(self):
        if self.average >= 9:
            self.rating = "XUAT SAC"
        elif self.average >= 8: self.rating = "GIOI"
        elif self.average >= 7: self.rating = "KHA"
        elif self.average >= 5: self.rating = "TB"
        else: self.rating = "YEU"
    def __str__(self):
        return self.id + ' ' + self.name + ' ' + ('%.1f'%self.average) + ' ' + self.rating
lst = []
for i in range(int(input())):
    name = input()
    point = [float(x) for x in input().split()]
    id = i+1
    lst.append(Student(name, point, 'HS%02d'%id))
for i in lst:
    i.tb()
    i.xh()
lst = sorted(lst, key=lambda x : x.average, reverse=True)
for i in lst:
    print(i)
# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0