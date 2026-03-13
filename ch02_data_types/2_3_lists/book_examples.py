### 점프 투 파이썬 02-3 리스트 자료형 예제 실습 ###


## 1. 리스트는 어떻게 만들고 사용할까?

# 리스트는 대괄호([])로 감싸 주고, 요솟값은 쉬표(,)로 구분한다

# 리스트명 = [요소1, 요소2, 요소3...]


## 2. 리스트의 인덱싱과 슬라이싱

# 1) 리스트의 인덱싱
print("=" * 50)
print("2-1 리스트의 인덱싱")
print("\n")

print("list_1_a = [1, 2, 3]")
list_1_a = [1, 2, 3]
print("list_1_a =", list_1_a)      # [1, 2, 3]
print("list_1_a[0] =",list_1_a[0]) # 1
print("list_1_a[0] + list_1_a[2] =", list_1_a[0] + list_1_a[2]) # 4
print("list_1_a[-1]", list_1_a[-1]) # 3
print("\n")

print("list_1_b = [1, 2, 3, ['a', 'b', 'c']]")
list_1_b = [1, 2, 3, ['a', 'b', 'c']]
print("list_1_b[0] =",list_1_b[0])                      # 1
print("list_1_b[-1] =",list_1_b[-1])                    # ['a', 'b', 'c']
print("list_1_b[3] =",list_1_b[3])                      # ['a', 'b', 'c']
print("list_1_b[-1][0] =",list_1_b[-1][0])              # a
print("list_1_b[-1][1] =",list_1_b[-1][1])              # b
print("list_1_b[-1][2] =",list_1_b[-1][2])              # c
print("\n")

print("삼중 리스트에서 인덱싱하기")
print("list_1_c = [1, 2, ['a', 'b', ['Life', 'is']]]")
list_1_c = [1, 2, ['a', 'b', ['Life', 'is']]]
print("list_1_c[2][2][0] =",list_1_c[2][2][0])            # Life
print("\n")

print("=" * 50)

# 2) 리스트의 슬라이싱
print("2-2 리스트의 슬라이싱")
print("\n")

print("list_2_a = [1, 2, 3, 4, 5]")
list_2_a = [1, 2, 3, 4, 5]
print("list_2_a[0:2] =",list_2_a[0:2])                # [1, 2]

print("list_2_b = list_2_a[:2]")
list_2_b = list_2_a[:2]

print("list_2_c = list_2_a[2:]")
list_2_c = list_2_a[2:]

print("list_2_b =",list_2_b)                     # [1, 2]
print("list_2_c =",list_2_c)                     # [3, 4, 5]
print("\n")

# 1분 코딩
# list_2_minA = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2, 3]을 만들어 보자.
print("1분 코딩")
print("list_2_minA = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2, 3]을 만들어 보자.")
list_2_minA = [1, 2, 3, 4, 5]
print("list_2_minA[1:3] =",list_2_minA[1:3])             # [2, 3]
print("\n")

# 중첩된 리스트에서 슬라이싱하기
print("중첩된 리스트에서 슬라이싱하기")
print("list_2_nesA = [1, 2, 3, ['a', 'b', 'c'], 4, 5]")
list_2_nesA = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print("list_2_nesA[2:5] =",list_2_nesA[2:5])                 # [3, ['a', 'b', 'c'], 4]
print("list_2_nesA[3][:2] =",list_2_nesA[3][:2])               # ['a', 'b']
print("\n")
print("=" * 50)


## 3. 리스트 연산하기
print("3. 리스트 연산하기")
print("\n")

# 1) 리스트 더하기[+]
print("3-1 리스트 더하기[+]")
list_3_1_a = [1, 2, 3]
list_3_1_b = [4, 5, 6]
print("list_3_1_a + list_3_1_b =", list_3_1_a + list_3_1_b) # [1, 2, 3, 4, 5, 6]

print("\n")
# 2) 리스트 반복하기[*]
print("3-2 리스트 반복하기[*]")
list_3_2_a = [1, 2, 3]
print("list_3_2_a * 3 =", list_3_2_a * 3)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print("\n")
# 3) 리스트 길이 구하기
print("3-3 리스트 길이 구하기")
list_3_3_a = [1, 2, 3]
print("len(list_3_3_a) =", len(list_3_3_a)) # 3

print("\n")
# 4) 초보자가 범하기 쉬운 리스트 연산 오류
print("3-4 초보자가 범하기 쉬운 리스트 연산 오류")
list_3_4_a = [1, 2, 3]
print("list_3_4_a = [1, 2, 3]")
print("list_3_4_a[2] =", list_3_4_a[2]) # 3
# print(list_3_4_a + "hi")  # error. 정수와 문자열은 더할 수 없다.
print("str(list_3_4_a[2]) + 'hi' =",str(list_3_4_a[2]) + "hi")    # 3hi. list_3_4_a[2]의 값을 문자로 변환해서 hi와 더할 수 있다.
print("\n")

print("=" * 50)

## 4. 리스트의 수정과 삭제

# 1) 리스트의 값 수정하기
print("4-1 리스트의 값 수정하기")
list_4_1_a = [1, 2, 3]
print("list_4_1_a[2] =", list_4_1_a[2]) # 3
print("print(list_4_1_a) =", list_4_1_a)

# list_4_1_a[2]의 값을 4로 수정 3 -> 4
list_4_1_a[2] = 4
print("list_4_1_a[2] =", list_4_1_a[2]) # 4
print("print(list_4_1_a) =", list_4_1_a)    # [1, 2, 4]
print("\n")

# 2) del 함수를 사용해 리스트 요소 삭제하기
print("4-2 del 함수를 사용해 리스트 요소 삭제하기")

list_4_2_a = [1, 2, 3]
print("list_4_2_a =", list_4_2_a)   # [1, 2, 3]
del list_4_2_a[1]
print("del list_4_2_a[1] = 2 삭제")
print("list_4_2_a =", list_4_2_a)   # [1, 3]
print("\n")

print("=" * 50)

## 5. 리스트 관련 함수

# 1) 리스트에 요소 추가하기 - append
print("5-1 리스트에 요소 추가하기 - append")

list_5_1_a = [1, 2, 3]
print("list_5_1_a =", list_5_1_a)   # [1, 2, 3]
print("list_5_1_a.append(4) = 4 추가")
list_5_1_a.append(4)
print("list_5_1_a =", list_5_1_a)   # [1, 2, 3, 4]
list_5_1_a.append([5, 6])
print("list_5_1_a.append([5, 6]) = [5, 6] 추가")
print("list_5_1_a =", list_5_1_a)   # [1, 2, 3, 4, [5, 6]]
print("\n")

# 2) 리스트 정렬 - sort
print("5-2 리스트 정렬 - sort")

list_5_2_a = [1, 4, 3, 2]
print("list_5_2_a =", list_5_2_a)   # [1, 4, 3, 2]
print("list_5_2_a.sort()")
list_5_2_a.sort()
print("list_5_2_a =", list_5_2_a)   # [1, 2, 3, 4]
print("─────────────────────────")

list_5_2_b = ['a', 'c', 'b']
print("list_5_2_b =", list_5_2_b)   # ['a', 'c', 'b']
print("list_5_2_b.sort()")
list_5_2_b.sort()
print("list_5_2_b =", list_5_2_b)   # ['a', 'b', 'c']
print("\n")

# 3) 리스트 뒤집기 - reverse
print("5-3 리스트 뒤집기 - reverse")

list_5_3_a = ['a', 'c', 'b']
print("list_5_3_a =", list_5_3_a)   # ['a', 'c', 'b']
list_5_3_a.reverse()
print("list_5_3_a.reverse()")
print("list_5_3_a =", list_5_3_a)   # ['b', 'c', 'a']
print("\n")

# 4) 인덱스 반환 - index
print("5-4 인덱스 반환 - index")

list_5_4_a = [1, 2, 3]
print("list_5_4_a =", list_5_4_a)   # [1, 2, 3]

list_5_4_a.index(3)
print("list_5_4_a.index(3) =", list_5_4_a.index(3)) # 2

list_5_4_a.index(1)
print("list_5_4_a.index(1) =", list_5_4_a.index(1)) # 0

print("\n")

# 5) 리스트에 요소 삽입 - insert
print("5-5 리스트에 요소 삽입 - insert")

list_5_5_a = [1, 2, 3]
print("list_5_5_a =", list_5_5_a)   # [1, 2, 3]
list_5_5_a.insert(0, 4)
print("list_5_5_a.insert(0, 4)")
print("list_5_5_a =", list_5_5_a)   # [4, 1, 2, 3]
print("─────────────────────────")

list_5_5_a.insert(3, 5)
print("list_5_5_a.insert(3, 5)")
print("list_5_5_a =", list_5_5_a)   # [4, 1, 2, 5, 3]

print("\n")

# 6) 리스트 요소 제거 - remove
print("5-6 리스트 요소 제거 - remove")

list_5_6_a = [1, 2, 3, 1, 2, 3]
print("list_5_6_a =", list_5_6_a)   # [1, 2, 3, 1, 2, 3]

list_5_6_a.remove(3)
print("list_5_6_a.remove(3)")
print("list_5_6_a =", list_5_6_a)   # [1, 2, 1, 2, 3]

list_5_6_a.remove(3)
print("list_5_6_a.remove(3)")
print("list_5_6_a =", list_5_6_a)   # [1, 2, 1, 2]

print("\n")

# 7) 리스트 요소 끄집어 내기 - pop
print("5-7 리스트 요소 끄집어 내기 - pop")

list_5_7_a = [1, 2, 3]
print("list_5_7_a =", list_5_7_a)   # [1, 2, 3]

print("list_5_7_a.pop() =", list_5_7_a.pop())   # 3
print("list_5_7_a =", list_5_7_a)   # [1, 2]

list_5_7_b = [1, 2, 3]
print("list_5_7_b.pop(1) =", list_5_7_b.pop(1)) # 2
print("list_5_7_b =", list_5_7_b)   # [1, 3]

print("\n")

# 8) 리스트에 포함된 요소 x의 개수 세기 - count
print("5-8 리스트에 포함된 요소 x의 개수 세기 - count")

list_5_8_a = [1, 2, 3, 1]
print("list_5_8_a =", list_5_8_a)   # [1, 2, 3, 1]
print("list_5_8_a.count(1) =", list_5_8_a.count(1)) # 2

print("\n")

# 9) 리스트 확장 - extend
print("5-9 리스트 확장 - extend")

list_5_9_a = [1, 2, 3]
print("list_5_9_a =", list_5_9_a)   # [1, 2, 3]
list_5_9_a.extend([4, 5])
print("list_5_9_a.extend([4, 5])")
print("list_5_9_a =", list_5_9_a)   # [1, 2, 3, 4, 5]

print("─────────────────────────")

list_5_9_b = [6, 7]
print("list_5_9_b =", list_5_9_b)   # [6, 7]
list_5_9_a.extend(list_5_9_b)
print("list_5_9_a.extend(list_5_9_b)")
print("list_5_9_a =", list_5_9_a)   # [1, 2, 3, 4, 5, 6, 7]