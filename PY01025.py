s = input()
s = s[::-1]
s = " " + s
ss = ""
for i in range(1, len(s)):
    ss += s[i]
    if i % 3 == 0 and i != len(s) - 1:
        ss += ","
ss = ss[::-1]
print(ss)