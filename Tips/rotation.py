def rotate_90(m):
    n = len(m)
    ret = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = m[r][c]
    return ret


def rotate_180(m):
    n = len(m)
    ret = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[n-1-r][n-1-c] = m[r][c]
    return ret


def rotate_270(m):
    n = len(m)
    ret = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[n-1-c][r] = m[r][c]
    return ret
