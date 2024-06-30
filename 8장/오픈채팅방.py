
def solution(record):
    
    dic = {}
    result = []
    for i in range(len(record)):
        sp = record[i].split()
        if sp[0] == 'Enter':
            dic[sp[1]] = sp[2]
        elif sp[0] == 'Change':
            dic[sp[1]] = sp[2]
    
    for i in range(len(record)):
        
        sp = record[i].split()
        if sp[0] == 'Enter':
            string = dic[sp[1]] + '님이 들어왔습니다.'
            result.append(string)
            
        elif sp[0] == 'Leave':
            string = dic[sp[1]] + '님이 나갔습니다.'
            result.append(string)

    
    return result
    




record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
