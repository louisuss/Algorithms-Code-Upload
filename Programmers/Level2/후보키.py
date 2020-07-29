from itertools import combinations
from collections import deque


def sol(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        # 이 부분이 핵심!!! 이부분에서 시간많이 걸림
        temp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(temp)) == n_row:
            final.append(keys)

    # 가능한 모든 조합
    answer = set(final)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            # 특정 조합의 길이 == 특정 조합과 다른 조합의 교집합 길이 => 삭제
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                # discard vs remove
                # remove 없는 값에 대해 제거 시 에러 발생
                # discard는 모든 경우에 대해 정상 작동
                answer.discard(final[j])
    return len(answer)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(sol(relation))
