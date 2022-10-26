def convert(num, k):
    res = 1
    if k == 4:
        res = 2
    elif k == 8:
        res = 3
    elif k == 16:
        res = 4
    num = "".join(reversed(num))
    ans = ""
    for index in range(0, len(num), res):
        tmp = int(num[index:index + res][::-1], 2)
        if tmp >= 10:
            ans += chr(ord('A') - 10 + tmp)
        else:
            ans += str(tmp)
    return ans[::-1]

test = int(input())
while test > 0:
    test -= 1
    k = int(input())
    num = input()
    print(convert(num, k))