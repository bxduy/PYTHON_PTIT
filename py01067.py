def solve():
    n = int(input())
    q = list()
    for i in range(1, 3):
        q.append(str(i))
    while n > 0:
        tmp = q[0]
        q.pop(0)
        if count_2(tmp):
            print(tmp, end=" ")
            n -= 1
        q.append(tmp + "0")
        q.append(tmp + "1")
        q.append(tmp + "2")

def count_2(num):
    return str(num).count("2") > len(str(num)) // 2


test = int(input())
for i in range(test):
    solve()
    print()