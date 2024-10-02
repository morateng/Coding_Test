N = 5
# 합이 5이면 멈춘다, 5를 초과하면 백트래킹
def solution(N):
    result = []
    
    def backtrack(sum, selected_nums, start):
        if sum == 10:
            result.append(selected_nums)
            return

        for i in range(start, N+1):
            if sum + i <= 10:
                backtrack(
                    sum+i, selected_nums + [i], i+1
                )
    backtrack(0, [], 1)
    return result

print(solution(N))