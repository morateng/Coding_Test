




def solution(nums):
    
    tree = set(nums)
    n = len(nums)//2

    return min(len(tree), n)




nums = [3,1,2,3]
print(solution(nums))
