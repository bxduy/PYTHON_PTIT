s = input()
cnt = 0
for i in range(0, len(s)):
    if s[i].islower():
        cnt = cnt+1
if cnt >= len(s)/2:
    s = s.lower()
else:
    s = s.upper()
print(s)