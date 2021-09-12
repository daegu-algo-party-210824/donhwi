n, m = map(int, input().split(" "))
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

INF = 999999999
d = [INF] * (m+1)
d[0] = 0

for i in range(m+1):
    for coin in coin_types:
        if i - coin >= 0:
            d[i] = min(d[i], d[i-coin] + 1)

print(d)

if d[m] is INF:
    print(-1)
else:
    print(d[m])