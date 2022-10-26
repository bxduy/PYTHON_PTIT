import math


class PS:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pstg(self):
        tmp = math.gcd(self.x, self.y)
        self.x /= tmp
        self.y /= tmp
    def __str__(self):
        return '{}/{}'.format(int(self.x), int(self.y))
if __name__ == '__main__':
    m, n = map(int, input().split())
    ps = PS(m, n)
    ps.pstg()
    print(ps)
