# list: 순서있고 중복허용하고 수정가능 삭제가능

a = [10, 100, 'pen', 'orange', 'apple']

print(a[0:3]) # 끝 인덱스는 범위에 포함되지 않음. -1이라고 생각해야함.
# 리스트 연산 가능

# 리스트 수정 삭제
c = [77, 2, 3, 4]
c[1:2] = [100, 1000, 10000]
print(c)    # [77, 100, 1000, 10000, 3, 4]

# 마지막 원소 지우기
del c[-1]

# 리스트 관련 함수
c.append(4) # 마지막에 원소 추가
c.extend([2, 3])    # append는 배열 자체를 넣는거고 extend는 배열 확장이라 원소만 들어감
c.sort() # 오름차순 정렬
c.reverse() # 내림차순 정렬
c.insert(2, 7)  # 2번 인덱스에 숫자 7 삽입
c.remove(2)     # 리스트 안의 2를 제거
c.pop() # 맨 마지막 요소를 꺼낸 후 나머지 반환

# tuple: 순서있고 중복허용하지만 수정, 삭제가 안됨
# 한번 들어가면 변경되면 안되는 데이터들, 중요한 값들에 사용

# 튜플 함수, 공통함수이기도 함
print(3 in [2, 3])  # 배열에 3이 있다면 True 반환
print(c.index(2))   # 2는 c라는 배열에서 몇 인덱스인가

# Dictionary : 순서 없음, 중복값 없음, 수정, 삭제 가능
c.values() # 키 말고 값만
c.sort# 키 값 다 가져옴 
# in, not in은 말 그대로 불리언을 반환함

# 집합(set) 순서 없음 중복 허용 안함
# 보통 형변환을 함으로 이용한다
a = set()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  # s1과 s2의 교집합
print(s1 & s2)  #intersection과 같음

print(s1.union(s2)) # 합집합. 중복값은 당연히 제외되고 나온다.
print(s1 | s2)  # union과 같음

print(s1.difference(s2))    # 차집합
print(s1 - s2)  # difference와 같음