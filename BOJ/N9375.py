from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    result = 1

    for i in range(n):
        name, category = input().split()
        arr.append(category)

    counter = Counter(arr)
    
    for item in counter.items():
        result *= (item[1] + 1)

    print(result - 1)
