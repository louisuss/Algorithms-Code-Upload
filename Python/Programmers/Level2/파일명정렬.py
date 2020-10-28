# 숫자 반영 정렬 기준
# 영문 대소문자, 숫자, ' ', . , -
# head 숫자아닌문자 - 최소 한글자 이상
# number - 한글자~다섯글자사이 연속된 숫자 - 0~99999
# tail - 나머지 부분, 없을 수도 있음


# 전처리
# 1. 문자 분해
# 2. 012 < 13 - 0이 숫자앞에 있는 경우 어떻게 할지 처리
# 3. 같을 경우 기존 순서 유지
def solution(files):
    files = sep(files)

    # 기존 순서 유지 부분 에러
    return merge(sorted(files, key=lambda x: (x[0].lower(), int(x[1]))))

# [(head, number, tail), ...]


def sep(files):
    sep_files = []
    check_number = [str(i) for i in range(10)]
    for file in files:
        head, number, tail = '', '', ''
        for f in file:
            if f not in check_number and number == '':
                head += f
                continue
            if f in check_number and tail == '':
                number += f
                continue
            tail += f
        sep_files.append((head, number, tail))
    return sep_files


def merge(files):
    merge_files = []
    for file in files:
        merge_files.append(file[0]+file[1]+file[2])

    return merge_files
