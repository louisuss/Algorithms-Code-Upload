# ababcdcdababcdcd ->2ab2cd2ab2cd ->2 ababcdcd
# abcabcdede -> abcabc2de ->2abcdede
# 1씩 증가하면서 묶기 -> 같은거 있으면 합치기 -> 길이 구하기
# 하나가 에러남 -> 길이가 1,2,3 일 때 예외처리하면 안남

def solution(s):
    def merge_len(var):
        cnt = 1
        temp = ''
        # 마지막인 경우 케이스 생각해야함
        for i in range(len(var)-1):
            if var[i] == var[i+1]:
                cnt += 1
                if (i+1) == len(var)-1:
                    temp += str(cnt) + var[i]
            else:
                if cnt > 1:
                    temp += str(cnt) + var[i]
                else:
                    temp += var[i]
                cnt = 1
                if (i+1) == len(var)-1:
                    temp += var[i+1]
        return len(temp)

    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 2
    elif len(s) == 3:
        return 3

    minimum = merge_len(s)

    for i in range(2, len(s)//2+1):
        temp = []

        for j in range(0, len(s), i):
            # 이 경우 이렇게 예외처리 안해도 제대로 잘려짐
            # if j+i-1 > len(s)-1:
            #     temp.append(s[j:])
            #     break
            temp.append(s[j:j+i])

        minimum = min(minimum, merge_len(temp))
    return minimum


# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


# def solution(text):
# [len(text)] -> text 길이가 1,2,3 인 경우 예외 때문에 입력해야함.
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])


