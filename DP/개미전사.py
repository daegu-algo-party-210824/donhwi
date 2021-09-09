# 답안지랑 다른 풀이
n = int(input())
k = list(map(int, input().split(" ")))

d = [0] * 100

d[0] = k[0]
d[1] = k[1]
d[2] = k[2] + k[0]

# 현재 i번째 식량창고를 무조건 털어야 한다고 가정했을때, 고려할 수 있는 것 = d[i-2], d[i-3]
for i in range(3, n):
    d[i] = max(k[i]+d[i-2], k[i]+d[i-3])

print(max(d))

"""
추가 테스트 케이스 
5
2 7 9 3 1
=> 12

4
1 2 3 1
=> 4
"""