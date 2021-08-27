s = input()
numbers = []

for i in s:
    numbers.append(int(i))

result = numbers[0]

for number in numbers[1:]:
    if number == 0 or result == 0:
        result += number
        continue
    
    result *= number

print(result)


