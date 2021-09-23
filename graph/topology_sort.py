"""
위상 정렬 = 방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것"
"""

from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A 에서 B로 이동 가능 
    # 진입차수를 1 증가 
    indegree[b] += 1

# 위상 정렬 함수 
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭개 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""

