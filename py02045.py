num = input()
if len(num) == 1:
    print(num)
else:
    while len(num) > 1:
        res = len(num) // 2
        tmp1 = num[:res]
        tmp2 = num[res:]
        num = str(int(tmp1) + int(tmp2))
        print(num)
