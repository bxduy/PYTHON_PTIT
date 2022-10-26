def check(ls):
    return ls[0] == ls[1] and ls[1] == ls[2] and ls[2] == ls[3]
while True:
    ls = [int(x) for x in input().split()]
    if ls[0] == 0 and check(ls):
        break
    cnt = 0
    while not check(ls):
        cnt += 1
        tmp = ls[0]
        for i in range(0, len(ls)-1):
            ls[i] = abs(ls[i] - ls[i+1])
        ls[3] = abs(ls[3] - tmp)
    print(cnt)