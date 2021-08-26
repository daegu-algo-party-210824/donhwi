n, m = map(int, input().split(" "))

result = 0
for _ in range(n):
    cards = map(int, input().split(" "))
    min_value = min(cards)
    
    if min_value > result:
        result = min_value

print(result)

