N, M = map(int, input().split())
map_list = []
for _ in range(N):
    map_list.append(list(map(int, input().split())))

solution_list = set()

def l():
    for i in range(M-3):
        for j in range(N):
            solution_list.add(map_list[j][i]+map_list[j][i+1]+map_list[j][i+2]+map_list[j][i+3])

    for i in range(N-3):
        for j in range(M):
            solution_list.add(map_list[i][j]+map_list[i+1][j]+map_list[i+2][j]+map_list[i+3][j])

def square():
    for i in range(N-1):
        for j in range(M-1):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i+1][j] + map_list[i+1][j+1])

def zigzag():
    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i+1][j] + map_list[i][j+1] + map_list[i+1][j+1] + map_list[i][j+2])

    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j] + map_list[i+1][j] + map_list[i+1][j+1] + map_list[i+2][j+1])

def op_zigzag():
    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j+1] + map_list[i+1][j+1] + map_list[i+1][j] + map_list[i+2][j])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i+1][j+1] + map_list[i+1][j+2])

def t():
    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j+1] + map_list[i+1][j] + map_list[i+1][j+1] + map_list[i+2][j+1])

    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j] + map_list[i+1][j] + map_list[i+2][j] + map_list[i+1][j+1])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j+1] + map_list[i+1][j] + map_list[i+1][j+1] + map_list[i+1][j+2])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i][j+2] + map_list[i+1][j+1])

def L():
    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j] + map_list[i+1][j] + map_list[i+2][j] + map_list[i+2][j+1])

    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i+1][j+1] + map_list[i+2][j+1])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i][j+2] + map_list[i+1][j])

    for j in range(M - 2):
        for i in range(N - 1):
            solution_list.add(map_list[i][j+2] + map_list[i+1][j] + map_list[i+1][j+1] + map_list[i+1][j+2])

def op_L():
    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i+2][j] + map_list[i+2][j+1] + map_list[i+1][j+1] + map_list[i][j+1])

    for j in range(M-1):
        for i in range(N-2):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i+1][j] + map_list[i+2][j])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j] + map_list[i+1][j] + map_list[i+1][j+1] + map_list[i+1][j+2])

    for j in range(M-2):
        for i in range(N-1):
            solution_list.add(map_list[i][j] + map_list[i][j+1] + map_list[i][j+2] +map_list[i+1][j+2])

l()
square()
zigzag()
op_zigzag()
t()
L()
op_L()

print(max(solution_list))

