with open('CONTACT.in') as f:
    lines = f.readlines()
sett = set()
for line in lines:
    sett.add(line.strip().lower())
sett = sorted(sett)
for i in sett:
    print(i)