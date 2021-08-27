n = int(input())
figures = list(map(int, input().split(" ")))
figures.sort()

count = 0
result = 0

for figure in figures:
    # 현재 그룹의 인원 추가
    count += 1

    if count >= figure: # 현재 그룹의 인원수가 현재 공포도 이상이면
        # 그룹 결성
        result += 1
        count = 0

print(result)

