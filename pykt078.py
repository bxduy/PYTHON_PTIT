t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a = sorted(a)
    max(a)