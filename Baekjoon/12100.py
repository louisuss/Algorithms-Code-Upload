from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# logic 생각
# 상하좌우 이동이 아닌 맵의 방향을 바꿔가면서 한방향으로만 보내는 방식으로 생각
# 90도 회전

def rotate(b, n):
    nb = deepcopy(b)
    for i in range(n):
        for j in range(n):
            nb[j][n-i-1] = b[i][j]
    return nb


# 2 2 2 2
# 4 0 4 0
# 한 행 합쳐주기
def convert(lst, n):
    new_list = [i for i in lst if i]

    for i in range(1, len(new_list)):
        # 합치기
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    # 나머지 부분을 0으로 다 채워줌
    return new_list + [0] * (n-len(new_list))

def dfs(n, b, cnt):
    # 최대값
    ret = max([max(i) for i in b])
    # 횟수 사용 다 했을 떄
    if cnt == 0:
        return ret

    # 회전1번 컨버트1번 -> 4 방향
    for _ in range(4):
        # 행 합친 것을 반복하여 모든 행에 대해서 수행한 x 배열
        x = [convert(i, n) for i in b]
        # 기존의 모양과 다른 경우 -> 합치기 가능한 경우
        if x != b:
            # 기존의 배열과 같은 경우 나올때까지 dfs
            ret = max(ret, dfs(n, x, cnt - 1))
        # 기존의 배열과 같은 경우 회전 -> 더이상 합치기가 수행안될 떄
        b = rotate(b, n)
    return ret

print(dfs(n,board,5))
