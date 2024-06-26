
def count_sort(arr, k):
    
    hashtable = [0] * (k + 1)
    
    for num in arr:
        if num <= k:
            hashtable[num] = 1
    return hashtable

def solution(arr, target):
    hashtable = count_sort(arr, target)
    
    for num in arr:
        complement = target - num
        if(
            complement != num
            and complement >= 0
            and complement <= target
            and hashtable[complement] == 1
        ):
            return True
    return False


arr = [1, 2, 3, 4, 8]
target = 6
print(solution(arr, target))