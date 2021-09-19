from collections import deque

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if distance[next] == INF:
                distance[next] = distance[now] + 1
                queue.append(next)

bfs(1)

max_value = max(distance[1:])
max_index = distance.index(max_value)
print(max_index, max_value, distance.count(max_value))


"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""