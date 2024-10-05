from collections import deque

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
arr_1 = [1,2,3]
arr_2 = [4,5,6]

def solution(arr1, arr2):
    result = []
    arr1 = deque(arr1)
    arr2 = deque(arr2)
    while(True):
        if arr1[0] < arr2[0]:
            result.append(arr1[0])
            arr1.popleft()
        elif arr1[0] > arr2[0]:
            result.append(arr2[0])
            arr2.popleft()
        if len(arr1) == 0:
            result += arr2
            break
        if len(arr2) == 0:
            result += arr1
            break
    return result
            
    
print(solution(arr_1, arr_2))