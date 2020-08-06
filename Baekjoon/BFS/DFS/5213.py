from collections import deque

n = int(input())
# t 값 + 1 -> 0번 배열 사용안하기 때문
m, t = n*2, n*n-n//2+1
# Adjacent matrix
a = [[0]*m for _ in range(n)]
# Level Map
b = [[0]*m for _ in range(n)]
# Adjacent List
v = [[] for _ in range(t)]
path = [0 for _ in range(t)]

# adjacent matrix
def init():
    temp = deque()
    temp2 = deque()
    for i in range(1, t):
        temp.extend(list(map(int, input().split())))
        temp2.extend([i] * 2)

    for i in range(n):
        for j in range(m):
            if i % 2 == 1 and (j == 0 or j == m - 1):
                a[i][j] = 0
                b[i][j] = 0
            else:
                a[i][j] = temp.popleft()
                b[i][j] = temp2.popleft()

# adjacent list
def graph():
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(n):
        for j in range(m):
            now = b[i][j]
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                nxt = b[ni][nj]

                # nxt 와 now 의 레벨이 다르고 인접한 값이 같으면 근접 리스트에 추가
                if now != nxt and a[i][j] == a[ni][nj]:
                    v[now].append(nxt)

def bfs(ans):
    q = deque([1])
    check = [False]*t
    check[1] = True
    while q:
        x = q.popleft()
        for nx in v[x]:
            if not check[nx]:
                # 번호 중 가장 큰 것 저장
                ans = max(ans, nx)
                check[nx] = True
                # 새로운 경로 해당 레벨에 이전 경로 저장
                path[nx] = x
                q.append(nx)
    return ans

def result(ans):
    p = [ans]
    x = ans
    while path[x]:
        x = path[x]
        p.append(x)
    print(len(p))
    p.reverse()
    for i in p:
        print(i, end=' ')

init()
graph()
result(bfs(0))