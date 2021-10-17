n = int(input())

stairs = [0] # 시작점 = 0을 추가해 주는것이 중요
dp = [0] * (n + 1)

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, n+1):
                # i-2 계단에서 한번에 올라오는 경우, 연속되면 안되므로 i-3 -> i-1 -> i 로 올라오는 경우 
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

    print(dp[n])
