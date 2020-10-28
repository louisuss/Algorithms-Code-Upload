

# from itertools import combinations

# 나의 문제풀이1

# def solution(number, k):
#     answer = []
#     number = list(number)
#     answer2 = []
#     for i in combinations(number, len(number) - k):
#         answer.append(i)
#     for i in answer:
#         answer2.append(int(''.join(i)))

#     return str(max(answer2))


# 나의 문제풀이2
# def solution(number, k):
#     answer = ''
#     number = list(map(int, number))
#     pos = len(number)-k
#     idx = 0
#     while pos:
#         pos -= 1
#         m = 0
#         m_idx = 0
#         for i in range(idx, len(number)-pos):
#             if m < number[i]:
#                 m = number[i]
#                 m_idx = i
#         idx = m_idx+1
#         answer += str(m)
#     return answer

# Solution 1
def solution(number, k):
    st = []

# number 에서 하나씩 뺀다
    for e in number:
        # st이 있고 st 끝이 들어온 수 보다 작고 삭제 횟수가 남아있는 경우
        while st and st[-1] < e and k > 0:
            st.pop()
            k -= 1

        st.append(e)

# 완료 후 k가 남아 있으면 뒤에서부터 없애고 k를 빼준다.
    while k > 0:
        st.pop()
        k -= 1

    answer = ''.join(st)
    return answer

# Solution 2
# 마지막 케이스 시간 초과

# def solution(number, k):
#     answer = ''
#     num = list(map(int, number))
#     idx = num.index(max(num[:k+1]))
#     while idx < k:
#         answer += str(max(num[idx:k+1]))
#         idx = num[idx:].index(max(num[idx:k+1]))+idx+1
#         k += 1
#         if k == len(number):
#             break
#     return answer + number[k:]
