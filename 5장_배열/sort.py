## problem1
def solution(arr):
    arr.sort()
    return arr

a = [1, -5, 2, 4, 3]
print(solution(a))
## problem2

def solution2(arr):
    arr = set(arr)
    arr = list(arr)
    arr.sort(reverse=True)
    return arr

arr1 = [4, 2, 2, 1, 3, 4]
print(solution2(arr1))

def solution3(arr):
    arr1 = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr1.append(arr[i] + arr[j])
    arr1 = sorted(set(arr1))
    return arr1

numbers = [2, 1, 3, 4, 1]
print(solution3(numbers))    