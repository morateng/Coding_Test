
s = '[)(]'

def solution(s):
    s = list(s)
    count = 0
    for i in range(len(s)):
        stack = [i for i in s]
        if isTrue(stack):
            count += 1
        s.append(s[0])
        del s[0]
    
    return count
    


def isTrue(s):
    while(len(s)):
        k = s.pop()
        if k == ']' and '[' in s:
            s.remove('[')
        elif k == ')' and '(' in s:
            s.remove('(')
        elif k == '}' and '{' in s:
            s.remove('{')
        else:
            break
    if len(s) == 0:
        return True
    else:
        return False
        

print(solution(s))