import datetime


def convert(s):
    return datetime.datetime.strptime(s, '%d/%m/%Y %H:%M')


map = dict()
with open('CATHI.in') as f:
    n = f.readline().strip()
    for i in range(int(n)):
        time1 = f.readline().strip()
        time2 = f.readline().strip()
        time = time1 + " " + time2

        id = 'C%03d' % (i + 1)
        map[id] = [time, f.readline().strip()]
for i in sorted(map.items(), key=lambda x: convert(x[1][0])):
    print(i[0], i[1][0], i[1][1])
