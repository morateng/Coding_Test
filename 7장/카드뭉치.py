from collections import deque

def solution(cards1, cards2, goal):
    
    result = 'Yes'
    card1 = deque()
    card2 = deque()
    goal_que = deque()
    
    for i in cards1:
        card1.append(i)
    for i in cards2:
        card2.append(i)
    for i in goal:
        goal_que.append(i)
    
    while(goal_que):
        if goal_que[0] == card1[0]:
            goal_que.popleft()
            front = card1.popleft()
            card1.append(front)
            
        elif goal_que[0] == card2[0]:
            goal_que.popleft()
            front = card2.popleft()
            card2.append(front)
        
        else:
            result = 'No'
            break
            
    return result

cards1 = ['i', 'water', 'drink']
cards2 = ['want', 'to']
goal = ['i', 'want', 'to', 'drink', 'water']

print(solution(cards1, cards2, goal))
    