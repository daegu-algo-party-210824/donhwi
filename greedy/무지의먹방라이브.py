"""
정확도 : 12.1
효율성 : 7.1
"""

def solution(food_times, k):

    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    food_times.sort()
    
    prev_rotate_num = 0
    while True:
        small_food = food_times[0][0]
        rotate_num = k // len(food_times)
        if rotate_num > small_food:
            rotate_num = small_food

        k -= len(food_times) * rotate_num

        index = 2001
        for i in range(len(food_times)):
            if food_times[i][0] > (prev_rotate_num + rotate_num):
                break
            if food_times[i][0] - (prev_rotate_num + rotate_num) == 0:
                index = i
        
        if index != 2001:
            for i in range(index+1):
                food_times.pop(i)

        # print(food_times)
        prev_rotate_num += rotate_num

        if k < len(food_times):
            break

    if not food_times:
        return -1

    food_times = sorted(food_times, key=lambda x : x[1])
    return food_times[k % len(food_times)][1]

print(solution([3,1,2], 5)) 
print(solution([4,2,3,6,7,1,5,8], 16))
print(solution([4,2,3,6,7,1,5,8], 27))
print(solution([3,1,1,1,2,4,3], 12))
print(solution([4,3,5,6,2], 7))
