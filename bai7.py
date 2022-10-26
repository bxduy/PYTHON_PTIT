import fileinput

for s in fileinput.input():
    if s == "":
        continue
    tmp = ""
    for i in range(0, len(s)):
        if s[i] != '.' and s[i] != '!' and s[i] != '?':
            tmp += s[i]
        else:
            ans = ""
            ls = tmp.split()
            for x in ls:
                ans += x + " "
            print(ans.capitalize())
            tmp = ""
# ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
#     vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.