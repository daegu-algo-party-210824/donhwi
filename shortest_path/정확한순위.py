n, m = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    distance[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distance[i][j] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

# ex) distance[a][b] = 2 이면, distance[b][a] = -2 로 세팅
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] != INF and distance[i][j] > 0:
            distance[j][i] = -distance[i][j]

count = 0
for i in range(1, n+1):
    if INF not in distance[i][1:]: # INF가 없어야 정확한 순위를 알 수 있다
        count += 1

print(count)