def search_matrix(matrix, target):
    # 예외 처리
    if not matrix:
        return False

    # 첫행의 맨뒤
    row = 0
    col = len(matrix[0]) - 1

    # 작으면 왼쪽, 크면 아래로 이동
    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False


def search_matrix2(matrix, target):
    return any(target in row for row in matrix)
