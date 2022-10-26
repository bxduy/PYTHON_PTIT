t = int(input())
while t > 0:
    t -= 1
    n = input()
    size = len(n)
    ls = []
    if size == 1:
        print(n)
    else:
        for i in range(0, size):
            ls.append(int(n[i]))
        for i in range(size-1, 0, -1):
            if ls[i] >= 5:
                ls[i-1] += 1
            ls[i] = 0
        for i in ls:
            print(i, end = "")
        print()




