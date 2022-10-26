def check(num):
    if int(num) % 7 == 0:
        return num
    for i in range(1, 1001):
        num = str(num)
        num = int(num) + int(num[::-1])
        if num % 7 == 0:
            return num
    return -1

test = int(input())
while test > 0:
    test -= 1
    s = input()
    print(check(s))