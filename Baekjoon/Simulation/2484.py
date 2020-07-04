def money():
    lst = sorted(list(map(int, input().split())))
    check = len(set(lst))

    if check == 1:
        return lst[0] * 5000 + 50000
    if check == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000+lst[1]*500+lst[2]*500
    if check == 3:
        for i in range(3):
            if lst[i] == lst[i+1]:
                return 1000 + lst[i]*100

    return lst[-1]*100


N = int(input())
print(max(money() for i in range(N)))


# sum = []
# for _ in range(N):
#     n = sorted(map(int, input().split()))
#     check = len(set(n))

#     if check == 1:
#         sum.append(50000+n[0]*5000)

#     # 같은 눈 3
#     # 같은 눈 2 * 2
#     if check == 2:
#         if n[1] == n[2]:
#             sum.append(10000+n[1]*1000)
#         else:
#             sum.append(2000+n[0]*500+n[-1]*500)

#     # 같은 눈 2 * 1
#     if check == 3:
#         for i in range(3):
#             if n[i] == n[i+1]:
#                 sum.append(1000 + n[i]*100)
#     if check == 4:
#         sum.append(n[-1]*100)

# print(max(sum))
