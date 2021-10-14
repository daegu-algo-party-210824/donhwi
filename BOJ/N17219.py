import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for _ in range(n):
    addr, password = input().split()
    dict[addr] = password

for _ in range(m):
    find_password = input().rstrip()
    print(dict[find_password])