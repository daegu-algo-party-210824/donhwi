from collections import deque

n, m = map(int, input().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

INF = 999999999

visited = [[INF] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1 and visited[nx][ny] == INF:
                queue.append((nx, ny))
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1

        print(visited)

bfs(0, 0, visited)

print(visited[n-1][m-1])