from collections import deque

n, k = map(int, input().split())
c = n // 4
data = deque(input())
solution = []

def move():
    temp = data.pop()
    data.appendleft(temp)

def split_number():
    temp = [[] for _ in range(4)]
    for i in range(4):
        # 0 3 / 3 6 / 6 9 / 9 12
        for j in range(c*i, c*(i+1)):
            temp[i].append(data[j])
        temp[i] = ''.join(map(str, temp[i]))
    return temp

for i in range(3):
    for j in split_number():
        solution.append(j)
    move()


solution = set(solution)
solution = list(solution)
solution.sort(reverse=True)

answer = 0
p = solution[k - 1]
p = p[::-1]
for s in range(c):
    if p[s] == 'A':
        answer += 10*(16**s)
    elif p[s] == 'B':
        answer += 11*(16**s)
    elif p[s] == 'C':
        answer += 12 * (16**s)
    elif p[s] == 'D':
        answer += 13*(16**s)
    elif p[s] == 'E':
        answer += 14*(16**s)
    elif p[s] == 'F':
        answer += 15*(16**s)
    else:
        answer += int(p[s])*(16**s)

print(answer)


