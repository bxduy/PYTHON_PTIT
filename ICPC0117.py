t = int(input())
sett = {"2", "3"}
sett.clear()
for i in range(0, t):
    s = input()
    sett.add(s)
print(len(sett))