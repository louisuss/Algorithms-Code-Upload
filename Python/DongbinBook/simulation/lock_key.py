m, n = map(int, input().split())
key = [list(map(int, input().split())) for _ in range(m)]
lock = [list(map(int, input().split())) for _ in range(n)]


def solution(key, lock):
    # 90도 회전
    def rotate_90(key):
        n = len(key)
        rot = [[0]*n for _ in range(n)]

        for r in len(n):
            for c in len(n):
                rot[c][n-1-r] = key[r][c]
        return rot
    # 맞는지 체크

    def check(new_lock):
        lock_length = len(new_lock) // 3
        for i in range(lock_length, lock_length*2):
            for j in range(lock_length, lock_length*2):
                if new_lock[i][j] != 1:
                    return False
        return True

    n = len(lock)  # lock 길이
    m = len(key)  # key 길이
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 중간에 위치시킴
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4방향에 대해 확인
    for rotation in range(4):
        key = rotate_90(key)
        # 0 ~ 2n - lock
        for x in range(n*2):
            # 0 ~ 2n
            for y in range(n*2):
                # 0 ~ m - key
                # 자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
