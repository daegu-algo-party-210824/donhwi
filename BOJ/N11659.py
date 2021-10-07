import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]

for i in range(n):
    sum_arr.append(sum_arr[i] + arr[i])

for _ in range(m):
    start, end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])
