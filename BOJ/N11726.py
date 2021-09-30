import sys 

input = sys.stdin.readline

n = int(input())
datas = list(map(int, input().split()))
data_set = list(sorted(set(datas)))
data_dict = {}

for index, value in enumerate(data_set):
    data_dict[value] = index

for data in datas:
    print(data_dict[data], end = " ")