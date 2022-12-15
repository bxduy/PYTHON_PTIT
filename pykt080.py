move_i = [-1, -1, -1, 0, 0, 1, 1, 1]
move_j = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m = map(int, input().split())
cnt = 0
statistic = [[0 for i in range(n+2)] for j in range(m+2)]
vis = [[False for i in range(n+2)] for j in range(m+2)]
for i in range(1, n+1):
    arr = [int(x) for x in input().split()]
    for j in range(1, m+1):
        statistic[i][j] = arr[j-1]
sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if statistic[i][j] == -1:
            for k in range(8):
                new_i, new_j = i+move_i[k], j+move_j[k]
                if vis[new_i][new_j] == False:
                    sum += statistic[new_i][new_j]
                    vis[new_i][new_j] = True
print(sum)