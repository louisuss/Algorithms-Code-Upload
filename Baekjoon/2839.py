n = int(input())

cnt = 0
while True:
    if n % 5 == 0:
        cnt += n//5
        break
    n = n-3
    cnt += 1
    if n < 0:
        print(-1)
        break



# n = int(input())
#
# for i in range(n//5,-1,-1):
#     a = n % (5*i)
#     if a % 3 == 0:
#         print(int(i+a/3))
#         break
#     else:
#         print(-1)
