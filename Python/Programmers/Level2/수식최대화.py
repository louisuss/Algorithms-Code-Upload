from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0
    op = set()
    sp = []
    num = ''

    # 숫자랑 연산자 분리
    for i in expression:
        if i in ['*', '+', '-']:
            sp.append(num)
            sp.append(i)
            op.add(i)
            num = ''
        else:
            num += i
    if num != '':
        sp.append(num)

    # 연산자 경우의 수
    opList = list(permutations(op, len(op)))

    # 연산자 경우의 수
    for i in opList:
        # 기존리스트 변하면 안되기 때문에 복사본 사용
        temp_sp = deepcopy(sp)
        # 연산자 하나씩 꺼냄
        for j in i:
            # 해당 연산자가 더 이상 없을 때 까지 반복
            while j in temp_sp:
                # 해당 연산자의 위치
                idx = temp_sp.index(j)
                # 연산자 좌우값 연산 후 해당 연산자 인덱스 전꺼에 입력
                if j == '*':
                    temp_sp[idx-1] = str(int(temp_sp[idx-1])
                                         * int(temp_sp[idx+1]))
                elif j == '+':
                    temp_sp[idx-1] = str(int(temp_sp[idx-1]) +
                                         int(temp_sp[idx+1]))
                else:
                    temp_sp[idx-1] = str(int(temp_sp[idx-1]) -
                                         int(temp_sp[idx+1]))

                # 연산자와 다음수 제거
                del temp_sp[idx]
                del temp_sp[idx]
        answer = max(answer, abs(int(temp_sp[0])))

    return answer
