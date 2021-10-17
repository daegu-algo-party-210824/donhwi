n = int(input())

factorial = 1

for i in range(2, n+1):
    factorial *= i

count = 0

factorial = str(factorial)

for i in range(len(factorial)-1, -1, -1):
    if factorial[i] != '0':
        break
    else:
        count += 1

print(count)
