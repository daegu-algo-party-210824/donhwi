import sys 
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 바이러스의 위치(x, y)를 바로 확인할 수 있도록 바이러스 리스트 생성
virus_list = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_list.append((i, j))

def virus(vx, vy, visited):
    queue = deque()
    queue.append((vx, vy))
    visited[vx][vy] = 1

    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1

count = 0
result = 0

# 벽 세우기
def select_wall(count):
    global result

    if count == 3:
        # 바이러스 확산
        visited = [[0] * m for _ in range(n)]
        for vx, vy in virus_list:
            virus(vx, vy, visited)

        # 안전영역 개수 구하기
        safety_zone = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0 and visited[i][j] == 0: # visited가 1인 경우는 바이러스가 퍼진 곳
                    safety_zone += 1
        if result < safety_zone:
            result = safety_zone
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                select_wall(count)
                graph[i][j] = 0
                count -= 1

select_wall(count)
print(result)
