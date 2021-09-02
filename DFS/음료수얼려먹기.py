from collections import deque

n, m = map(int, input().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]
count = 0

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1

        print(queue)

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and visited[x][y] == 0:
            bfs(x, y, visited)
            count += 1

print(count)