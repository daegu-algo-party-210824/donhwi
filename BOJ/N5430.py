"""
* 주의할점 
output -> [2, 1]과 [2,1]은 다른것
아웃풋 출력에 주의
"""

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cals = list(input().rstrip())
    n = int(input())
    
    if n == 0:
        arr = list(input().strip("[").rstrip().strip("]"))
    else:
        arr = list(map(int, input().strip("[").rstrip().strip("]").split(",")))

    point1 = 0
    point2 = n
    reverse = 1 # 1: 뒤집히지 않은 상태, -1: 뒤집은 상태

    for cal in cals:
        if cal == "D" and reverse == 1:
            point1 += 1
            if point1 > point2:
                print("error")
                break
        elif cal == "D" and reverse == -1:
            point2 -= 1
            if point2 < point1:
                print("error")
                break
        elif cal == "R":
            reverse *= -1
    else: # output
        if reverse == 1:
            result = "["
            for i in range(point1, point2):
                if i == point2-1:
                    result += str(arr[i])
                else:
                    result += str(arr[i])
                    result += ","
            result += "]"
            print(result)
        else:
            result = "["
            for i in range(point2-1, point1-1, -1):
                if i == point1:
                    result += str(arr[i])
                else:
                    result += str(arr[i])
                    result += ","
            result += "]"
            print(result)


"""
1
D
1
[1]

[]
"""