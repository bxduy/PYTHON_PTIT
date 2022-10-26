def fee(name, num, sta):
    if sta == 'OUT':
        return 0
    if name == 'Xe_con':
        if num == 5:
            return 10000
        return 15000
    if name == 'Xe_tai':
        return 20000
    if name == 'Xe_khach':
        if num == 29:
            return 50000
        return 70000
map = dict()
data = list()
for i in range(int(input())):
    arr = input().split()
    num = int(arr[2])
    if arr[4] in map:
        map[arr[4]] = map[arr[4]] + fee(arr[1], num, arr[3])
    else:
        data.append(arr[4])
        map[arr[4]] = fee(arr[1], num, arr[3])
for i in data:
    print(i + ":", end=" ")
    print(map[i])
# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 OUT 08/11/2021