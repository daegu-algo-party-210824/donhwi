n, m = map(int, input().split())

graph = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def dfs(x, y, cnt, sum_value):
    global result

    if cnt == 4:
        result = max(result, sum_value)
        return

    visited[x][y] = 1
    sum_value += graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0: 
            dfs(nx, ny, cnt + 1, sum_value)
    
    visited[x][y] = 0


T5 = [[0, 0], [0, 1], [0, 2], [1, 1]]
T5_UD = [[0, 0], [1, -1], [1, 0], [1, 1]]
T5_R90 = [[0, 0], [1, 0], [2, 0], [1, -1]]
T5_R270 = [[0, 0], [1, 0], [2, 0], [1, 1]]

def sum(x, y, T):
    global result
    s = 0

    for i in range(4):
        if 0 <= x + T[i][0] < n and 0 <= y + T[i][1] < m:
            s += graph[x + T[i][0]][y + T[i][1]]
    
    result = max(result, s)


for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0)
        sum(i, j, T5)
        sum(i, j, T5_UD)
        sum(i, j, T5_R90)
        sum(i, j, T5_R270)

print(result)