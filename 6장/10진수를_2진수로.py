
def solution(decimal):
    
    stack = []
    while(True):
        num = decimal // 2
        remain = decimal % 2
        stack.append(remain)
        decimal = num
        if decimal == 1:
            stack.append(1)
            break
    stack.reverse()
    return stack

print(solution(12345))