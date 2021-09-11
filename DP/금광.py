t = int(input())

for _ in range(t):
    n, m = map(int, input().split(" "))
    array = list(map(int, input().split(" ")))

    d = []
    for i in range(n):
        d.append(array[i*m:(i*m)+m])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                d[j][i] = max(d[j][i]+d[j][i-1], d[j][i]+d[j+1][i-1])
            if j == 1:
                d[j][i] = max(d[j][i]+d[j-1][i-1], d[j][i]+d[j][i-1], d[j][i]+d[j+1][i-1])
            if j == 2:
                d[j][i] = max(d[j][i]+d[j-1][i-1], d[j][i]+d[j][i-1])

    print(max(map(max, d)))