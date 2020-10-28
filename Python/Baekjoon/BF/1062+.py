N, K = map(int, input().split())
K = K - 5


def dfs(idx, cnt):
    global answer

    # 글자수 사용 다 한 경우
    if cnt == K:
        print(learn)
        read_cnt = 0
        for word in words:
            for w in word:
                # 해당 단어 중 안 배운 알파벳 있으면 break
                if not learn[ord(w)-ord('a')]:
                    break
            # word가 비어있는 경우
            # break 동작 안했을 때 작동
            else:
                read_cnt += 1
        answer = max(answer, read_cnt)
        return

    for i in range(idx, 26):
        # 알파벳 중 안 배운거 체크
        if not learn[i]:
            learn[i] = True
            # 배울 수 있는 글자 수 다 쓰기
            dfs(i, cnt + 1)
            # dfs 진행 후 배운거 취소
            learn[i] = False


if K < 0:
    print(0)
elif K == 26:
    print(N)
else:
    words = []
    answer = 0
    for _ in range(N):
        # 중복제거
        word = set(input()[4:-4])
        temp = set()
        # 특정 알파벳 제거
        for w in word:
            if w not in ['a', 'n', 't', 'c', 'i']:
                temp.add(w)
        # 길이가 K 보다 작아야 읽을 수 있음
        if len(temp) <= K:
            words.append(temp)

    # 알파벳
    learn = [False] * 26
    # 읽은 알파벳 체크
    for l in ['a', 'n', 't', 'c', 'i']:
        learn[ord(l)-ord('a')] = True

    dfs(0, 0)
    print(answer)
