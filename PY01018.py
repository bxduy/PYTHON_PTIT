def decode(s, k):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    s = str(s)
    k = int(k)
    ans = ""
    for i in range(0, len(s)):
        ans += P[(P.find(s[i]) + k) % 28]
    return ans[::-1]


while True:
    ls = [str(i) for i in input().split()]
    if len(ls) == 1:
        break
    print(decode(ls[1], ls[0]))