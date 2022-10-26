class Rectangle:
    def __init__(self, height, width, mau):
        self.height = height
        self.width = width
        self.mau = mau

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def color(self):
        return self.mau.lower().capitalize()



arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print('INVALID')
