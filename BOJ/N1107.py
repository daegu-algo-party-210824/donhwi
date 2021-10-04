"""
brute force 
for-else문
"""

import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

if m != 0:
    broken = set(input().split())
else:
    broken = set()

# 현재 채널에서 '+', '-' 버튼으로만 움직이는 경우
min_cnt = abs(100 - n)

# 작은 수에서 큰수로 이동할대는 500000까지만 보면 되지만,
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1000000까지 확인
for num in range(1000001):
    for str_num in str(num):
        if str_num in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우 
            break
    else:
        # min(기존값, 번호를 누른 횟수 + 해당 번호로부터 채널까지의 차이)
        min_cnt = min(min_cnt, len(str(num)) + abs(num - n))

print(min_cnt)