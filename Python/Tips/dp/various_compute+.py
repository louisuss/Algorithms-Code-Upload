def various_compute(strs):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                print("  ", l, r, op)
                results.append(eval(str(l)+op+str(r)))
        return results

    if strs.isdigit():
        return [int(strs)]

    result = []
    for idx, val in enumerate(strs):
        if val in "-+*":
            print(strs[:idx], strs[idx+1:], val)
            left = various_compute(strs[:idx])
            right = various_compute(strs[idx+1:])

            result.extend(compute(left, right, val))
    return result


print(various_compute("2*3-4*5"))
