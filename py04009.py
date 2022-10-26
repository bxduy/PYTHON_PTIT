class SP:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __str__(self):
        a = abs(self.thuc)
        b = abs(self.ao)
        if self.ao > 0:
            return '{} + {}i'.format(self.thuc, self.ao)
        else:
            return '{} - {}i'.format(self.thuc, b)
def add(sp1:SP, sp2:SP):
    thuc = sp1.thuc + sp2.thuc
    ao = sp1.ao + sp2.ao
    return SP(thuc, ao)
def mul(sp1:SP, sp2:SP):
    thuc = sp1.thuc*sp2.thuc - sp1.ao*sp2.ao
    ao = sp1.thuc*sp2.ao + sp2.thuc*sp1.ao
    return SP(thuc, ao)
for i in range(int(input())):
    a = [int(x) for x in input().split()]
    sp1 = SP(a[0], a[1])
    sp2 = SP(a[2], a[3])
    sp3 = add(sp1, sp2)
    sp4 = mul(sp3, sp1)
    sp5 = mul(sp3, sp3)
    print(sp4, ", ", sp5, sep="")