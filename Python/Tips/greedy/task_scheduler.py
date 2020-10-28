from collections import Counter

# Counter -> most_common, subtract, Counter() 초기화 기능 활용


def least_interval(tasks, n):
    counter = Counter(tasks)
    result = 0

    while True:
        sub_cnt = 0
        # 자기포함하기 때문에 +1
        for task, _ in counter.most_common(n+1):
            sub_cnt += 1
            result += 1

            counter.subtract(task)
            counter += Counter()

        # counter 비는 경우. 종료
        if not counter:
            break

        # idle 채울 부분
        result += n + 1 - sub_cnt

    return result
