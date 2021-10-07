import sys 

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

""" 50점
p = "I"
for i in range(n):
    p += "OI"

count = 0
i = 0 # 문자열의 index 0부터 검사
while i < m - (n * 2):
    print(i)
    if p == s[i:i+len(p)]: # O(N*M) 시간 복잡도가 걸린다
        count += 1
        i += 2
    else:
        i += 1

print(count)
"""

p_count = 0
total_count = 0

i = 1
while i < m-1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
        p_count += 1
        i += 2
    else:
        i += 1
        p_count = 0
    
    if p_count == n:
        total_count += 1
        p_count -= 1

print(total_count)
    




