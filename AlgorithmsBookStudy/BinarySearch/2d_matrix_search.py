def search_matrix(matrix, target):
    # 예외 처리
    if not matrix:
        return False

    # 첫 행의 맨뒤
    row = 0
    col = len(matrix[0])-1

    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True

        # 타켓이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1
        # 타겟이 크면 아래로 이동
        elif target > matrix[row][col]:
            row += 1
    return False

# pythonic-way


def search_matrix_pythonic(matrix, target):
    return any(target in row for row in matrix)
