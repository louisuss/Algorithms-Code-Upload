# push 순서가 오름차순 유지
# push+ pop-

# 순서대로 진행해서 qustions과 비교 같은게 있으면 pop
# flag로 참거짓 체크 / 현재 인덱스 체크
n = int(input())

# # 질문 리스트
# question = [int(input()) for _ in range(n)]
# # 정답 리스트
# answer = []
# # push
# temp = []
# idx = 0
# for i in range(1, n+1):
#     temp.append(i)
#     answer.append('+')

#     while temp[-1] == question[idx]:
#         temp.pop()
#         answer.append('-')
#         idx += 1

#         # 임시 리스트가 비었거나 다 찾은경우
#         if not temp or idx == n:
#             break

# if idx == n:
#     for v in answer:
#         print(v)
# else:
#     print('NO')

n = int(input())

cnt = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    # 입력된 데이터까지 스택에 넣기
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        result.append('+')

    # 데이터와 끝값이 일치
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))
