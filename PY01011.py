ls = []
def check(n):
    m = n
    cnt = 0
    s = 0
    while n > 0:
        tmp = n % 10
        if tmp != 0 and tmp != 2 and tmp != 4 and tmp != 6 and tmp != 8:
            return False
        cnt += 1
        s = s * 10 + tmp
        n //= 10
    if cnt % 2 != 0:
        return False
    if m != s:
        return False
    return True
def solve():
    for i in range(22, pow(10, 8), 22):
        if check(i):
            ls.append(i)
solve()

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(0, len(ls)):
        if ls[i] < n:
            print(ls[i], end=" ")
        else:
            break
    print()
