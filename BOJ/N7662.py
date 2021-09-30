import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    minpq = []
    maxpq = []
    visit = [False] * 1000000 # False = 어떤 힙에서 삭제된 상태 

    for i in range(k):
        cal, n = input().split()

        if cal == "I":
            heapq.heappush(minpq, (int(n), i))
            heapq.heappush(maxpq, (-int(n), i))
            visit[i] = True
        elif cal == "D":
            if n == "-1":
                while minpq and not visit[minpq[0][1]]: # 어떤 힙에서 삭제된 것 제거 
                    heapq.heappop(minpq)
                if minpq:
                    visit[minpq[0][1]] = False  
                    heapq.heappop(minpq)
            else:
                while maxpq and not visit[maxpq[0][1]]: # 어떤 힙에서 삭제된 것 제거
                    heapq.heappop(maxpq)
                if maxpq:
                    visit[maxpq[0][1]] = False
                    heapq.heappop(maxpq)

    # 마지막 연산 수행 후 동기화
    while minpq and not visit[minpq[0][1]]:
        heapq.heappop(minpq)
    while maxpq and not visit[maxpq[0][1]]:
        heapq.heappop(maxpq)

    if minpq:
        max = -maxpq[0][0]
        min = minpq[0][0]
        print(max, min)
    else:
        print("EMPTY")



    