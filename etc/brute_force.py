"""
* 브루트 포스 알고리즘 
검색 대상이 되는 원본 문자열의 처음부터 끝까지 차례대로 순회하며 문자들을 일일이 비교하는 방식의 고지식한 알고리즘
비교하고자 하는 문자열과 패턴을 한 칸씩 이동하면서 비교하여 일치 여부를 확인합니다
"""

def BruteForce(p, t):
    i = 0 # t의 검색 인덱스
    j = 0 # p의 검색 인덱스
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1


pattern = "Python"
text = "Hello Python World"
print(BruteForce(pattern, text))