n, m = map(int, input().split(" "))
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

INF = 999999999
d = [INF] * 10001
d[0] = 0

for coin in coin_types:
    d[coin] = 1

for i in range(n):
    for j in range(coin_types[i], m+1):
        d[j] = min(d[j], d[j-coin_types[i]] + 1)

if d[m] is INF:
    print(-1)
else:
    print(d[m])