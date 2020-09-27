def solution(flowers):
    answer = 0
    # 누적되는 부분 계산
    start, end = 0, 0
    len_flower = len(flowers)

    check = False
    for idx in flowers:
        now_start, now_end = flowers[idx][0], flowers[idx][1]
        next_start, next_end = flowers[idx+1][0], flowers[idx+1][1]

        # 겹치는 부분이 아직 없는 경우
        if not check:
            start, end = now_start, now_end

        # 겹치는 부분 발생
        if next_start <= now_end:
            # 마지막 부분 갱신
            end = next_end
            check = True
        else:
            # 이전에 중복된 부분 더하기
            if check:
                answer += end - start
                check = False
            else:
                answer += now_end - now_start

    # 마지막 경우가 위의 조건에 포함안됨
    # 중복이 없는 경우 마지막 더하기
    if check:
        answer += flowers[len_flower-1][1] - flowers[len_flower-1][0]
    # 중복된 경우 누적된 결과 더하기
    else:
        answer += end - start

    return answer
