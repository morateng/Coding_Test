
def solution(answers):
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answers_list = [0, 0, 0]
    
    while(len(first) < len(answers)):
        first = first * 2
    while(len(second) < len(answers)):
        second = second * 2
    while(len(third) < len(answers)):
        third = third * 2
    
    for i in range(len(answers)):
        if first[i] == answers[i]:
            answers_list[0] += 1
        if second[i] == answers[i]:
            answers_list[1] += 1
        if third[i] == answers[i]:
            answers_list[2] += 1

    max_val = max(answers_list)
    index_list = []
    for i in range(len(answers_list)):
        if answers_list[i] == max_val:
            index_list.append(i+1)
            
    
    return index_list

answers = [1, 3, 2, 4, 2]
print(solution(answers))    
    
    
