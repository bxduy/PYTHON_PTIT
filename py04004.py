import math

def object(tu, mau):
    return PS(tu, mau)

class PS:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pstg(self):
        tmp = math.gcd(self.x, self.y)
        self.x /= tmp
        self.y /= tmp
    def add(self, PS):
        mau = self.y * PS.y
        tu = self.x * PS.y + self.y * PS.x
        return object(tu, mau)
    def __str__(self):
        return '{}/{}'.format(int(self.x), int(self.y))
a = [int(x) for x in input().split()]
p = PS(a[0], a[1])
q = PS(a[2], a[3])
tmp = p.add(q)
tmp.pstg()
print(tmp)
