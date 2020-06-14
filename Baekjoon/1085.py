x, y, w, h = map(int, input().split())
print(min([x, y, w-x,h-y]))
# x, y, w, h = map(int, input().split())
#
# mid_x = w/2
# mid_y = h/2
#
# if x > mid_x and y > mid_y:
#     if h-y > w-x:
#         print(w-x)
#     else:
#         print(h-y)
# elif x < mid_x and y > mid_y:
#     if x > h-y:
#         print(h-y)
#     else:
#         print(x)
# elif x <= mid_x and y <= mid_y:
#     if x > y:
#         print(y)
#     else:
#         print(x)
# else:
#     if w-x > y:
#         print(y)
#     else:
#         print(w-x)
#
