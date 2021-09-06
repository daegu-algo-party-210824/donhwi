from collections import deque

n, k = map(int, input().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(" "))))
s, x, y = map(int, input().split(" "))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# <시간초과>
# virus_list = [[] for _ in range(k+1)]
# for i in range(n):
#     for j in range(n):
#         virus_number = graph[i][j]
#         if virus_number != 0:
#             virus_list[virus_number].append((i, j))
# 
# seconds = 0
# while seconds < s:
#     # 바이러스 리스트에서 낮은 번호의 바이러스부터 상,하,좌,우로 퍼트린다
#     for i in range(1, k+1):
#         virus_num = len(virus_list[i]) # i번 바이러스의 개수
#         for j in range(virus_num):
#             vx, vy = virus_list[i][j]
#             for d in range(4):
#                 nx = vx + dx[d]
#                 ny = vy + dy[d]
#                 if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
#                     graph[nx][ny] = i # i = 바이러스 번호
#                     virus_list[i].append((nx, ny)) # 퍼트린 바이러스를 바이러스 리스트에 추가
#         virus_list[i][virus_num:] # 바이러스를 퍼트린 바이러스를 바이러스 리스트에서 제거한다(한번 바이러스를 퍼트리면 해당 바이러스는 바이러스를 또 퍼트리지 않아도 된다)
#     seconds += 1

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j], i, j, 0)) # (바이러스번호, x, y, 시간)

queue.sort()
queue = deque(queue)

while queue:
    virus_num, vx, vy, seconds = queue.popleft()
    if seconds >= s:
        break

    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus_num
            queue.append((virus_num, nx, ny, seconds+1))


print(graph[x-1][y-1])


