# 배열 갱신이 잦아지는 경우 global로 전역변수로 해결하는게 좋음
def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    # set으로 중복없애서 남은 수가 1개인경우는 모든수가 같다는 얘기
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for i in range(int(input())):
    process()


# 원
# 처음 홀수개 가지고 있는 아이 사탕 보충
# 반 오른쪽으로 줌
# 홀수개 사탕 가지고 있는 아이 생기면 한개 보충

# from collections import deque

# T = int(input())

# kids = []
# for _ in range(T):
#     N = int(input())
#     temp = list(map(int, input().split()))
#     for idx, t in enumerate(temp):
#         if t % 2 != 0:
#             temp[idx] += 1
#     kids.append(temp)


# def check_diff(a):
#     for i in range(1, len(a)):
#         if a[i-1] != a[i]:
#             return True
#     return False


# for kid in kids:
#     cnt = 0

#     if len(kid) == 1:
#         print(cnt)
#         continue

#     while check_diff(kid):
#         half_kid = []
#         for k in kid:
#             half_kid.append(k//2)
#         add_kid = deque(half_kid)
#         # add_kid = add_kid.appendleft(add_kid.pop()) (X)
#         # add_kid = list(add_kid.appendleft(add_kid.pop())) (X)
#         add_kid.appendleft(add_kid.pop())

#         new_kid = []
#         for a, b in zip(half_kid, list(add_kid)):
#             sum = a+b
#             if sum % 2 != 0:
#                 sum += 1
#             new_kid.append(sum)
#         kid = new_kid
#         cnt += 1
#     print(cnt)
