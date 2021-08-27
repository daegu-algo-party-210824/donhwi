from collections import Counter
s = input()

numbers = []
num = s[0]
numbers.append(num)

# 연속된 숫자를 한 덩어리로 본다

for i in s[1:]:
    if num != i: # 같은 숫자가 아닐때만 numbers 리스트에 추가 후 num을 바꿔줌
        numbers.append(i)
        num = i

count = Counter(numbers)
result = min(count['0'], count['1'])
print(result)

