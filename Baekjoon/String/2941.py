a = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']
n = input()

for i in a:
    n = n.replace(i, '*')
print(len(n))

# n = input()
# list = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']
# count = 0
# for i in list:
#     if i in n:
#         count+=1
#         n = n.replace(i, '')
# print(count+len(n))

