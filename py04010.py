class Student:
    def __init__(self, name, bir, p1, p2, p3):
        self.name = name
        self.bir = bir
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __str__(self):
        return '{} {} {}'.format(self.name, self.bir, "%.1f"%(self.p3+self.p1+self.p2))
a = []
for i in range(5):
    a.append(input())
for i in range(2, 5):
    a[i] = float(a[i])
stu = Student(a[0], a[1], a[2], a[3], a[4])
print(stu)
