n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

white = 0
blue = 0

def dfs(x1, x2, y1, y2, n):
    global white, blue
    value = graph[x1][y1]
    
    if n == 1:
        if value == 1:
            blue += 1
        else:
            white += 1
        return

    breaker = False

    for i in range(x1, x2):
        for j in range(y1, y2):
            if graph[i][j] != value:
                dfs(x1, x1 + n//2, y1, y1 + n//2, n//2) # 1사분면
                dfs(x1, x1 + n//2, y1 + n//2, y2, n//2) # 2사분면
                dfs(x1 + n//2, x2, y1, y1 + n//2, n//2) # 3사분면
                dfs(x1 + n//2, x2, y1 + n//2, y2, n//2) # 4사분면
                breaker = True
                break
        if breaker:
            breaker = False
            break
    else:
        if value == 1:
            blue += 1
        else:
            white += 1

dfs(0, n, 0, n, n)

print(white)
print(blue)