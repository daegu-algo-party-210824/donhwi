"""
BOJ N9095 1,2,3 더하기
DP의 타일링 문제와 동일한 접근법
dp[i]를 구하는 경우, 
마지막으로 사용할 숫자로 1을 쓰고 싶을때는 dp[i-1] 
+ 2를 쓰고 싶을때는 dp[i-2] 
+ 3을 쓰고 싶을때는 dp[i-3]
"""

t = int(input())

dp = [1] * 11
dp[1] = 1
dp[2] = 2
for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    print(dp[int(input())])

