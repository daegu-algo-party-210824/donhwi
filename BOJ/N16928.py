from collections import deque

n, m = map(int, input().split())

INF = int(1e9)
graph = [0] * 101
visited = [INF] * 101

for _ in range(n): # 사다리
    start, end = map(int, input().split())
    graph[start] = end
    
for _ in range(m): # 뱀
    start, end = map(int, input().split())
    graph[start] = end

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        now = q.popleft()
        for i in range(1, 7):
            next = now + i
            if next <= 100 and visited[next] == INF:
                visited[next] = min(visited[next], visited[now] + 1)
                if graph[next] != 0: # 뱀 또는 사다리이면
                    next = graph[next]
                    q.append(next)
                    visited[next] = min(visited[next], visited[now] + 1)
                else:
                    q.append(next)

bfs(1)
print(visited[100])

