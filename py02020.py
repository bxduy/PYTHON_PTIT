n = int(input())
ls = [float(x) for x in input().split()]
sum = 0.0
cnt = 0
for x in ls:
    if x != min(ls) and x != max(ls):
        sum += x
        cnt += 1
print("{:.2f}".format(sum/cnt))