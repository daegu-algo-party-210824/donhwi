n = int(input())
t_list = []
p_list = []

for _ in range(n):
    t, p = map(int, input().split(" "))
    t_list.append(t)
    p_list.append(p)

d = [0] * n 

for i in range(n):
    if i + t_list[i] <= n:
        d[i] += p_list[i]
        for j in range(i + t_list[i], n):
            d[j] = max(d[j], d[i])

print(max(d))

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""