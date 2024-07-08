
def solution(want, number, discount):
    
    dic = {}
    count = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        discount_10d = {}
        
        for j in range(i, i+10):
            if discount[j] in dic:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1
        
        if discount_10d == dic:
            count += 1            
    return count
    


want = ['banana', 'apple', 'rice', 'pork', 'pot']
number = [3,2,2,2,1]
discount = ['chicken', 'apple', 'apple', 'banana', 'rice', 'apple', 'pork', 'banana', 'pork', 'rice', 'pot',
            'banana', 'apple', 'banana']

print(solution(want, number, discount))