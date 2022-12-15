map = dict()
for i in range(int(input())):
    arr = input().lower().split()
    for x in arr:
        tmp = ''
        for i in x:
            if 'a' <= i <= 'z':
                tmp += i
            elif '0' <= i <= '9':
                continue
            else:
                if tmp != '':
                    if tmp in map:
                        map[tmp] = map[tmp] + 1
                    else:
                        map[tmp] = 1
                tmp = ''
        if tmp != '':
            if tmp in map:
                map[tmp] = map[tmp] + 1
            else:
                map[tmp] = 1
map = sorted(map.items(), key=lambda x: (-x[1], x[0]))
for i in map:
    print(i[0], i[1])
# 3
# PTI1T duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT1 trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.