for _ in range(int(input())):
    k = int(input())
    n = int(input())
    v = [i for i in range(1,n+1)]
    for _ in range(k):
        for j in range(1,n):
            v[j] += v[j-1]
    print(v[n-1])


# def fun(k, n):
#     if k == 0:
#         return n
#     sum = 0
#     for i in range(1, n+1):
#         sum += fun(k-1,i)
#     return sum
# test_case = int(input())
# for _ in range(test_case):
#     k = int(input())
#     n = int(input())
#
#     print(fun(k,n))