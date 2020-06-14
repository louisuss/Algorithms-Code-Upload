# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# n = int(input())
# print(fibo(n))

n = int(input())
f0, f1 = 0, 1
for i in range(n):
    f0, f1 = f1, f0+f1
print(f0)