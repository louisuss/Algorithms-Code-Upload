import sys
# 크레인 무게 제한 / 박스 무게
# 6 8 9
# 2 2 4 5 7

# 3
# 2 3 9
# 5
# 2 2 4 5 7
n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))


def solution1():
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    turn = 0
    # 크레인 최대 감당 무게 < 박스 무게
    if cranes[0] < boxes[0]:
        print(-1)
    else:
        # 박스 다 처리할 때 까지 반복
        while boxes:
            # 크레인 한번씩 사용
            for crane in cranes:
                # 박스가 존재하는 경우
                if boxes:
                    # 처음 박스 체크를 무거운거부터 크레인이 옮길수 있는 것 찾기
                    idx = 0

                    # index 오류 while 문에서 많이 발생해서 시간뺏김.
                    while crane < boxes[idx]:
                        if idx >= len(boxes)-1:
                            break
                        idx += 1
                    # 박스 배에 옮기기
                    if crane >= boxes[idx]:
                        boxes.remove(boxes[idx])
                    else:
                        break

            # 시간
            turn += 1
        print(turn)


def solution2():
    if max(cranes) < max(boxes):
        print(-1)
        sys.exit()

    # 크레인이 현재 옮겨야하는 박스 번호
    crane_positions = [0]*n
    # 박스 옮겼는지 여부
    check_box_moved = [False]*m
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    result = 0
    count = 0

    while True:
        if count == len(boxes):  # 박스 다옮긴 경우
            break
        for i in range(n):
            while crane_positions[i] < len(boxes):  # 현재 크레인이 모든 박스 위치 탐색
                # 아직 안 롬긴 박스중에서, 옮길 수 있는 박스 만날 때까지 반복
                if not check_box_moved[crane_positions[i]] and cranes[i] >= boxes[crane_positions[i]]:
                    check_box_moved[crane_positions[i]] = True
                    crane_positions[i] += 1
                    count += 1
                    break
                crane_positions[i] += 1  # 옮긴 후 다음 박스 위치 가리키기
        result += 1
    print(result)


solution2()
