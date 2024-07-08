
def hash_f(string_list):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in string_list:
        hash_value = (hash_value * p + ord(char)) % m
    
    return hash_value

def solution(string_list, query_list):
    
    hash_list = [hash_f(str) for str in string_list]
    
    result = []
    for query in query_list:
        query_hash = hash_f(query)
        
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
            
    return result


string_list = ['apple', 'banana', 'cherry']
query_list = ['banana', 'kiwi', 'melon', 'apple']

print(solution(string_list, query_list))