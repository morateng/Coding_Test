
n_1 = 3
words_1 = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']

n_2 = 5
words_2 = ['hello', 'observe', 'effect', 'take']

n_3 = 2
words_3 = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
def solution(n, words):
    count = [0 for _ in range(n)]
    seq = []
    for i,k in enumerate(words):
        count[(i)%n] += 1
        if k in seq:
            return [(i%n)+1, count[i%n]]
        elif len(seq)>0 and k[0] != seq[i-1][-1]:
            return [(i%n)+1, count[i%n]]
        else:
            seq.append(k)
    return [0,0]
print(solution(n_2, words_2))