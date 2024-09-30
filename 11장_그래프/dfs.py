from collections import defaultdict

graph = [['A', 'B'], ['B', 'C'],['C', 'D'],['D', 'E']]
start = 'A'

def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for neigbor in adj_list.get(node, []):
            if neigbor not in visited:
                dfs(neigbor, visited, result)
    
    visited = set()
    result = []
    dfs(start, visited, result)
    return result

print(solution(graph, start))        

