lst = sorted(list(map(int, input().split())))
check = len(set(lst))

if check == 1:
    print(10000 + lst[0]*1000)
elif check == 2:
    print(1000 + lst[1]*100)
else:
    print(100*lst[2])

# n = list(map(int, input().split()))

# a = set(n)

# if len(a) == 1:
#     print(10000+n[0]*1000)
# elif len(a) == 2:
#     if n[0] == n[1]:
#         print(1000+n[0]*100)
#     elif n[0] == n[2]:
#         print(1000+n[0]*100)
#     elif n[1] == n[2]:
#         print(1000+n[1]*100)

# else:
#     print(max(a)*100)
