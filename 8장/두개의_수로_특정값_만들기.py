
def solution(arr, target):
    add_arr = []
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            add_arr.append(arr[i] + arr[j])
    
    if target in add_arr:
        return True
    else:
        return False

arr = [2, 3, 5, 9]
target = 10

print(solution(arr, target))
    
    