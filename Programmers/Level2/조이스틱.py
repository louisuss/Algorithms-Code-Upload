# ABAB -> 다음꺼가 A이면 카운트만
# ABBABAA
# JAB -> 다음꺼가 A이면 뒤로 이동이 나음
# JBA -> 끝이 A이면 다음꺼로 이동하는게 나음
# A가 연속된 경우가 문제
def solution(name):
    answer = 0
    idx = 0
    name = list(name)
    base = ['A'] * len(name)

    while True:
        left = 1
        right = 1

        # 현재 위치 왼쪽으로 갈지 오른쪽으로 갈지 결정
        if name[idx] != 'A':
            answer += min((ord(name[idx])-ord('A')), ord('Z')-ord(name[idx])+1)
            # 'A'이면 다시 이과정을 반복안함.
            name[idx] = 'A'

        # JEROEN
        # ABABAA -> 좌 우 커서 이동 중 A가 연속으로 없는 곳으로 이동
        if name == base:
            break
        else:
            for i in range(1, len(name)):
                if name[idx+i] == 'A':
                    right += 1
                else:
                    break
                if name[idx-i] == 'A':
                    left += 1
                else:
                    break

            if right > left:
                answer += left
                idx -= left
            else:
                answer += right
                idx += right

    return answer

# def solution(name):
#     answer = 0
#     idx = 0

#     while name != 'A'*len(name):
#         left = idx
#         right = idx

#         # 현재 위치 왼쪽으로 갈지 오른쪽으로 갈지 결정
#         if name[idx] != 'A':
#             answer += min((ord(name[idx])-ord('A')), ord('Z')-ord(name[idx])+1)
#             # 'A'이면 다시 이과정을 반복안함.
#             name = name[0:idx] + 'A' + name[(idx+1):]

#         # 기본 조건
#         if name == 'A'*len(name):
#             break

#         # JEROEN
#         # ABABAA -> 좌 우 커서 이동 중 A가 연속으로 없는 곳으로 이동
#         cnt = 1
#         while name[idx+cnt] == 'A':
#             right += 1
#             cnt += 1
#         cnt = 1
#         while name[idx-cnt] == 'A':
#             left += 1
#             cnt += 1

#         if right > left:
#             answer += left
#             idx -= left
#         else:
#             answer += right
#             idx += right

#     return answer
