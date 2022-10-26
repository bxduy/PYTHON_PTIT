t = int(input())
while t > 0:
    t -= 1
    s = input()
    check = True
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")