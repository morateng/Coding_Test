
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

def solution(participant, completion):
    dic = {}
    for i in participant:
        dic[i] = 0
    for i in participant:
        dic[i] += 1
    for i in completion:
        dic[i] -= 1
    
    for key in dic.keys():
        if dic[key] == 1:
            return key
    

print(solution(participant, completion))