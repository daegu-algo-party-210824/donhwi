"""
접두사 합 : 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓은 것 

1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장한다 
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L-1] 이다.
"""

n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세 번쨰 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
