from collections import deque

t = int(input())
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n = int(input())
    graph = []
    visited = [[INF] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = graph[0][0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + graph[nx][ny]

    print(visited[n-1][n-1])


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""