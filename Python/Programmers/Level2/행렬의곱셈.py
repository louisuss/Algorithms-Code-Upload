
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         lst = []
#         for j in range(len(arr2[0])):
#             sum = 0
#             for k in range(len(arr2)):
#                 sum += arr1[i][k] * arr2[k][j]
#             lst.append(sum)
#         answer.append(lst)
#     return answer

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


B = [[1, 2], [3, 4], [5, 6]]
for b_col in zip(*B):
    print(b_col)

new_list = list(map(list, zip(*B)))
print(new_list)
