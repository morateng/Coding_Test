from collections import deque
import math

def solution(progress, speeds):
    
    remain_time = deque()
    sol = []
    for i in range(len(progress)):
        remain_time.append(math.ceil((100-progress[i]) / speeds[i]))
    
    while(remain_time):
        front = remain_time.popleft()
        count = 1
        while(remain_time and remain_time[0] <= front):
            remain_time.popleft()
            count += 1
        sol.append(count)
        
    return sol
    

progress = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progress, speeds))