import heapq

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

n, k = map(int, input().split())
# 바이러스 리스트 정보
virus_info = [list(map(int, input().split())) for _ in range(n)]
# 종료시간, 결과 위치
s, x, y = map(int, input().split())
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(s, x, y, n):
    time = 0
    q = []
    # 초기큐
    for i in range(n):
        for j in range(n):
            if virus_info[i][j] != 0:
                # 번호가 낮은 순서로 바이러스가 번식되게 하기 위해 우선순위 큐 사용
                heapq.heappush(q, (virus_info[i][j], (i, j)))

    # 종료시간까지 루핑
    while time <= s:
        time += 1
        new_q = []
        # 큐에 있는 만큼 바이러스 번식.
        while q:
            virus = heapq.heappop(q)
            for r, c in dirs:
                nr, nc = virus[1][0] + r, virus[1][1] + c
                if 0 <= nr < n and 0 <= nc < n:
                    if virus_info[nr][nc] == 0:
                        virus_info[nr][nc] = virus[0]
                        heapq.heappush(new_q, (virus[0], (nr, nc)))
        # 다음 큐로 변경
        q = new_q
    return virus_info[x][y]


print(bfs(s, x-1, y-1, n))
