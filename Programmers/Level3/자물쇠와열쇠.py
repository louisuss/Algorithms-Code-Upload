def rotate(maps):
    return [list(reversed(i)) for i in zip(*maps)]


def solution(key, lock):
    hole = 0
    # hole 개수 총합
    for y in range(len(lock)):
        for x in range(len(lock[0])):
            if lock[y][x] == 0:
                hole += 1

    for _ in range(4):
        # 길이가 3 인경우 -2 ~ 5
        for start_y in range(-len(key)+1, len(lock)):
            for start_x in range(-len(key)+1, len(lock[0])):
                # 자물쇠와 lock 일치하는 개수
                ck = 0
                match = True
                for y in range(start_y, start_y + len(key)):
                    if y < 0 or y >= len(lock):
                        continue
                    for x in range(start_x, start_x+len(key[0])):
                        if x < 0 or y >= len(lock[0]):
                            continue
                        # 자물쇠 돌기와 열쇠 돌기가 만나는 경우
                        if lock[y][x] == 1 and key[y-start_y][x-start_x] == 1:
                            match = False
                            break

                        # 자물쇠 돌기와 홈 구멍이 일치하는 경우
                        if lock[y][x] == 0 and key[y-start_y][x-start_x] == 1:
                            check += 1

                    if not match:
                        break

                if match and check == hole:
                    return True
        key = rotate(key)
    return False


# def check_match(key, lock):
#     for i in range(len(lock)):
#         for j in range(len(lock)):
# 		# hole + hole / 튀 + 튀 인 경우
#             if lock[i][j] + key[i][j] != 1:
#                 return False
#     return True


# def solution(key, lock):
#     answer = True
#     key_len = len(key)
#     lock_len = len(lock)

#     new_key = []
# # lock 크기의 새로운 키 4개 -> 회전한 경우
#     for _ in range(4):
#         new_key.append([[0]*lock_len for _ in range(lock_len)])

#     for i in range(key_len):
#         for j in range(key_len):
# 		# 회전 4번
#             new_key[0][i][j] = key[i][j]
#             new_key[1][j][key_len-i-1] = key[i][j]
#             new_key[2][key_len-i-1][key_len-j-1] = key[i][j]
#             new_key[3][key_len-j-1][i] = key[i][j]

#     for key in new_key:
#         for i in range(lock_len):
#             for j in range(lock_len):
#                 left_up_key = [row[i:] + [0] *
#                                i for row in key[j:]] + [[0]*lock_len]*j
#                 if check_match(left_up_key, lock):
#                     return True
#                 left_down_key = [
#                     [0]*lock_len]*(lock_len-j-1) + [row[i:] + [0]*i for row in key[:j+1]]
#                 if check_match(left_down_key, lock):
#                     return True
#                 right_up_key = [[0]*i + row[:lock_len-i]
#                                 for row in key[j:]] + [[0]*lock_len]*j
#                 if check_match(right_up_key, lock):
#                     return True
#                 right_down_key = [[0]*lock_len]*(lock_len-j-1) + [[0]*i + row[:lock_len-i]
#                                                                   for row in key[:j+1]]
#                 if check_match(right_down_key, lock):
#                     return True
#     return False
