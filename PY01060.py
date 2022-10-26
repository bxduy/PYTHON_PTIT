def mul(num):
    mul = 1
    check = True
    for i in range(0, len(num), 2):
        if int(num[i]) != 0:
            check = False
            mul *= int(num[i])
    if check:
        return 0
    return mul

def sum(num):
    sum = 0
    for i in range(1, len(num), 2):
        sum += int(num[i])
    return sum

t = int(input())
while t > 0:
     t -= 1
     num = input()
     print(f"{mul(num)} {sum(num)}")