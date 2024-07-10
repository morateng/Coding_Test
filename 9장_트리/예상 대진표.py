import math

def solution(N, A, B):
    rounds = 1
    
    while(True):
        
        if ((B-A == 1 and A % 2 == 1) or (A-B == 1 and B % 2 == 1)):
            return rounds
        A = math.ceil(A / 2)
        B = math.ceil(B / 2)
        rounds += 1
        
    return rounds

N = 8
A = 4
B = 7

print(solution(N, A, B))