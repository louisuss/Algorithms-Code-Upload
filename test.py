def various_compute(strs):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l)+op+str(r)))
        return results

    if strs.isdigit():
        return [int(strs)]
    result = []
    for idx, val in enumerate(strs):
        if val in "-+*":
            left = various_compute(strs[:idx])
            right = various_compute(strs[idx+1:])

            result.extend(compute(left, right, val))
    print(result)
    return result


various_compute("2-1-1")
