
from collections import deque

t1 = [[1, 2], [3, 4], [5, 6], [-1, 7], [8, 9],
      [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
t2 = [[-1, -1]]


def solutions(t1, t2):
    answer = 0
    def pattern_append(a, b):
        temp = []
        if a == -1:
            temp.append(False)
        else:
            temp.append(True)
        if b == -1:
            temp.append(False)
        else:
            temp.append(True)
        return temp
    
    pattern = [True]
    for t in t2:
        a, b = t
        pattern += pattern_append(a, b)
    
    for node in range(len(t1)):
        temp = [True]
        q = deque([node])
        while len(temp) != len(pattern):
            a, b = t1[q.popleft()]
            q.append(a)
            q.append(b)
            temp += pattern_append(a, b)


        if temp == pattern:
            answer += 1

    return answer

print(solutions(t1,t2))