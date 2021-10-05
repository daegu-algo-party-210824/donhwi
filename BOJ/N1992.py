n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

result = ""

def quad_tree(n, x, y):
    global result
    
    color = graph[x][y]

    mix = False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                mix = True
                break


    if mix:
        result = result + "("
        quad_tree(n//2, x, y) # 왼쪽 위
        quad_tree(n//2, x, y + n//2) # 오른쪽 위
        quad_tree(n//2, x + n//2, y) # 왼쪽 아래
        quad_tree(n//2, x + n//2, y + n//2)
        result = result + ")"
    else:
        if graph[x][y] == "0":
            result += "0"
        elif graph[x][y] == '1':
            result += "1"

quad_tree(n, 0, 0)

print(result)

"""
4
0001
0010
0111
0111
"""