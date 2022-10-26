import Member
import Team
n, m = map(int, input().split())
dataT = list()
dataM = list()
for i in range(n):
    idT = i+1
    dataT.append(Member())