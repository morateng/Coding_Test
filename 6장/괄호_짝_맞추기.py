def solution(s):
    stack = []
    for i,k in enumerate(s):
        stack.append(k)
        if len(stack) > 1:
      
            if stack[len(stack)-1] == ')' and stack[len(stack)-2] == '(':
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False
    

s = '((())()'
print(solution(s))

        
    