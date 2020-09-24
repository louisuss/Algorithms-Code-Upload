from bisect import bisect_right, bisect_left

# frodo front frost frozen frame kakao
# fro?? ????o fr??? fro??? pro?

words = list(input().split())
queries = list(input().split())
# Solution1
def count_by_range(a, left_val, right_val):
    right_idx = bisect_right(a, right_val)
    left_idx = bisect_left(a, left_val)
    return right_idx - left_idx

# 단어를 길이마다 나눠서 저장하기 위한 리스트
arr = [[] for _ in range(10001)]
# 길이마다 뒤집어 저장 위한 리스트
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    result = []
    for word in words:
        w_len = len(word)
        arr[w_len].append(word) # 단어 삽입
        reversed_arr[w_len].append(word[::-1]) # 단어 뒤집어서 삽입

    # 길이별 단어 리스트 정렬
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    
    for query in queries:
        q_len = len(query)
        # 마지막글자
        if query[0] != '?':
            # "froaa", "frozz"
            res = count_by_range(arr[q_len], query.replace('?', 'a'), query.replace('?', 'z'))
        # 첫글자
        else:
            res = count_by_range(reversed_arr[q_len], query[::-1].replace('?', 'a'), query[::-1].replace('?','z'))
        result.append(res)
    return result
print(solution(words, queries))

# Solution2 - 시간초과
def solution2(words, queries):
    result = []
    for query in queries:
        cnt = 0
        for word in words:
            query = list(query)
            word = list(word)
            # 길이 같음
            if len(query) == len(word):
                check = 0
                # 문자 비교
                for a, b in zip(query, word):
                    if a == b or a == '?':
                        check += 1
                if check == len(query):
                    cnt += 1
        result.append(cnt)

    return result

print(solution2(words, queries))