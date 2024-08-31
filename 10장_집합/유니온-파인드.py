

def union(parents, x, y): # 두 집합을 합치는 함수
    root1 = find(parents, x)
    root2 = find(parents, y)
    
    parents[root2] = root1
    
    
def find(parents, x):
    # 루트 노드 찾는 함수
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

    
    
def solution(k, operations):
    parents = list(range(k))
    n = k
    
    for op in operations:
        if op[0] == 'u':
            union(parents, op[1], op[2])
        elif op[0] == 'f':
            find(parents, op[1])
    
    n = len(set(find(parents, i) for i in range(k)))
    
    return n

k = 3
operations = [['u',0,1], ['u',1,2], ['f',2]]
print(solution(k, operations))