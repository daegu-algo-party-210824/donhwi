import itertools

l, c = map(int, input().split())
vowels = ["a", "e", "i", "o", "u"]

data = list(input().split())
data.sort()

for x in itertools.combinations(data, l):
    code = "".join(list(x))
    count = 0
    for vowel in vowels:
        if vowel in code:
            count += 1
    
    if 0 < count <= l-2:
        print(code)


