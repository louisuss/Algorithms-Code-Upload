from bisect import bisect_left, bisect_right


def count_by_range(a, left_val, right_val):
    right_idx = bisect_right(a, right_val)
    print(right_idx)
    left_idx = bisect_left(a, left_val)
    print(left_idx)
    return right_idx - left_idx
arr = ["frame", "frodo", "front", "frost", "kakao"]
i = "fro??"
res = count_by_range(arr, i.replace('?', 'a'), i.replace('?', 'z'))
print(res)
