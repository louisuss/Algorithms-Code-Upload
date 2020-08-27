def daily_temp(T):
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        # 위치 저장
        stack.append(i)
    return answer
