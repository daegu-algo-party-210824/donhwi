n, m, k = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort(reverse=True)

result = 0

while True:
    if m == 0:
        break
    
    if m <= k:
        result += (numbers[0] * m)
        break
    else:
        result += (numbers[0] * k)
        result += numbers[1]
        m = m - (k + 1)
        print(result, m)

print(result)