def check(num):
    if len(num) % 2 == 0:
        return False
    if num[0] == num[1]:
        return False
    for i in range(2, len(num), 2):
        if num[i] != num[0]:
            return False
    return True

t = int(input())
while t > 0:
     t -= 1
     num = input()
     print("YES" if check(num) else "NO")