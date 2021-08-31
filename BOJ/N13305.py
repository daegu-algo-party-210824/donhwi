"""
BOJ N13305 주유소
"""

n = int(input())
distances = list(map(int, input().split(" ")))
distances.append(0)
prices = list(map(int, input().split(" ")))

n_price = prices[0]
# 초기화 - 첫번째 도시에서 이동 거리 * 기름 가격
result = distances[0] * n_price 

for i in range(1, len(prices)-1):
    if n_price > prices[i]: # 작은 기름 가격으로 n_price를 갱신
        n_price = prices[i]
    
    result += (distances[i] * n_price)

print(result)

