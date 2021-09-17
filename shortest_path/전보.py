import sys
import heapq

n, m, c = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for i in graph[now]:
            if distance[i[0]] > time + i[1]:
                distance[i[0]] = time + i[1] 
                heapq.heappush(q, (time + i[1], i[0]))

        # print(q)
        # print(distance)

dijkstra(c)

count = 0
max_time = 0
for d in distance:
    if d != 0 and d != INF:
        count += 1
        max_time = max(max_time, d)

print(count, max_time)




