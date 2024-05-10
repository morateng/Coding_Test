
def solution(N, stages):
    # 스테이지별 도전자 수
    challenger = [0] * (N+2)
    for stage in stages:
        challenger[stage] += 1

    fails = {} # 실패율 저장 딕셔너리
    total = len(stages)
    
    for i in range(1, N+1):
        if challenger[i] == 0:  # 도전자가 없는 스테이지는 실패율 0
            fails[i] = 0
        else:
            fails[i] = challenger[i]/total  # 실패율
            total -= challenger[i]  # 다음스테이지 도전자만 골라낸다
            
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
