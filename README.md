# Algorithms-Code-Upload

알고리즘 풀이 공유 목적

백준, 프로그래머스, Codility 등의 알고리즘 사이트에서 푼 문제 풀이 업로드

######### 문제 풀이 ###########
시간 엄수!!!
문제 꼼꼼히 이해
입력 조건 -> 복잡도 통과 범위 선택
문제에 적용할 알고리즘 선택
과정 그리기
최대한 함수 분리
코딩 시 문제 인덱스 범위 통일!!
디버깅

######## 문자열 처리 #########

문자열 슬라이싱 활용하기!! - 속도 유리, 매번 새로운 객체를 생성하기 떄문에 큰 배열의 경우 시간 느려짐.
문자열 -> 리스트 -> ''.join(list) 속도 많이 소요
a = [1, 2, 3, 4]
print(''.join(map(str, a)))
문자열 뒤집기 - strs[::-1]

문자열 정렬
sort -> 리스트만 사용가능
sorted(문자열) -> 문자하나하나 값인 리스트로 변경
sort, sorted -> 리스트로 변경된 것은 ''.join(list)로 문자열로 복구, lambda 활용 - 조건 두개인 경우 ()로 묶기, key = len 과 같은 함수 지정 가능
a = "52345"
print(sorted(a))

Counter() 활용
from collections import Counter
a = Counter(list) -> key(단어):value(개수) (dict 타입)
a.keys(), a.values(), a.items()
Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
가장 빈번한 단어 찾기 - most_common(개수) -> [('ball', 2)] -> most_common(개수)[0][0] - 단어 / most_common(개수)[0][1] - 카운트
-> Counter 값을 heap으로 만든 후 뽑으면 순서대로 출력

Counter 교집합으로 공통 부분 추출 가능
t = Counter(["a", "b", "c","b"])
b = Counter(["a", "b", "b"])
print(t & b) -> Counter({'b': 2, 'a': 1})

Counter 목록 제거 방법 - 값이 0인부분에 + Counter() 하면 0인 값드리 제거됨
t = Counter(["a", "b", "c", "b"])
b = Counter(["a", "b", "b"])
t.subtract("b")
t.subtract("b")
t += Counter()
print(t)
Counter({'a': 1, 'c': 1})

isalnum() - 영문자, 숫자 여부 판별
isalpha() - 알파벳인지 체크
isdigit() - 숫자 체크
lower() - 소문자 변환
upper() - 대문자 변환
chr(number) - 해당 아스키 번호 문자로 변경
ord('char') - 알파벳 범위 표현할 때 range(ord('A'), ord('Z')+1)
any([True, False, False]) -> True / all([True, False, True]) -> False

############ Hash #############
Seperate Chaining - 충돌 시 연결리스트로 저장
Open Addressing - 충돌 시 빈공간 찾아 저장 (모든 원소가 반드시 자신의 해시값과 일치하는 주소에 저장된다는 보장 없음)
-> 선형탐사 - 순차적 탐색 (고르게 분포안되고 뭉치는 경향 - 클러스터링(연속된 데이터 그룹))
-> 버킷 사이즈보다 큰 경우 삽입 불가 -> 버킷 크기 큰거 생성 후 새롭게 복사 (리해싱 작업) - 슬롯의 80%이상이 차게 되면 성능 저하

특정 개수 더하기 활용
키값으로 찾고자하는 단어, 값에 해당 단어의 반복수 -> Counter

########### DFS/BFS ####################
DFS - 재귀(백트래킹), 스택
-> 백트래킹

- 탐색을 하다가 더 갈 수 없으면 왔던 길을 되돌아가 다른 길을 찾음. 불필요한 부분을 일찍 포기하여 탐색 최적화. 트리의 탐색 최적화 문제와 연관
- 제약 충족 문제(수많은 제약 조건을 충족하는 상태 찾는 문제)에 활용. 스도쿠, 십자말 풀이, 8퀸 문제, 4색 문제 (퍼즐문제), 배낭 문제, 문자열 파싱, 조합 최적화 문제
  BFS - 큐 -> 최단 거리 구할 때 활용
  방문한 곳 다시 방문하지 않기 - 마킹, 값 제거

########## 스택/큐 ##########
사용시 비는경우 항상 체크

############ 슬라이딩 윈도우 ###############

투포인터 - 대부분 정렬된 배열 대상, 윈도우 사이즈가 가변적, 좌우 포인터가 자유롭게 이동하는 방식(양방향)
슬라이딩 윈도우 - 정렬 여부 상관 없음, 윈도우 사이즈 고정, 좌 또는 우 한방향으로만 이동(단방향)
-> 해당 범위내의 최대, 최소값 구할 때 활용

########### 그리디 ################
최적의 해
우선순위 큐 활용

bisect
bisect_left - 찾아낸 값의 인덱스, 없는 경우 해당 값이 들어갈 위치 출력
bisect_right - 찾아낸 값의 다음 인덱스

############## DP ################
조건: 1. 큰 문제를 작은 문제로 나눌 수 있다. 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
-> 큰 문제를 작게 나누고 같은 문제라면 한번씩만 풀어 해결하는 알고리즘 기법.
DP vs 분할 정복
-> DP 는 문제들이 서로 영향을 미침.
탑다운(메모이제이션) - 재귀 이용. 한번 구한 결과를 메모리 공간에 메모 (캐싱)
바텀업 - 반복문 이용. 작은 문제부터 답을 도출.

완전 탐색 알고리즘 적용 시 시간 초과, 해결하고자 하는 부분 문제들의 중복 여부 확인 -> DP 고려
knapsack 완벽 이해!!
한정 분기 알고리즘

########## 이진 탐색 ############
이진 탐색 트리 - 정렬된 구조를 저장하고 탐색
이진 검색 - 정렬된 배열에서 값을 찾아내는 것

파라메트릭 서치 - 원하는 조건을 만족하는 가장 알맞은 값 찾기 문제 (ex.가장큰값, 떡길이 문제)
