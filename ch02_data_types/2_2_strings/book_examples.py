# 점프 투 파이썬 02-2 문자열 자료형 예제 실습
# 문자열 생성, 이스케이프 코드, 인덱싱/슬라이싱, 포매팅, 문자열 함수 정리

### 문자열은 어떻게 만들고 사용할까?

# 1. 큰따옴표로 양쪽 둘러싸기
"Hello World"

# 2. 작은따옴표로 양쪽 둘러싸기
'Python is fun'

# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''


### 문자열 안에 따옴표나 큰따옴표를 포함시키고 싶을 때

# 1. 문자열에 작은따옴표 포함하기

# 'Python'이 문자열로 인식되어 구문 오류가 발생함.
# food = 'Python's favorite food is perl'

# 2. 문자열에 큰따옴표 포함하기
food_1 = "Python's favorite food is perl"
print(food_1)   # Python's favorite food is perl

# 3. 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
food_2 = 'Python\'s favorite food is perl'
say_2 = "\"Python is very easy.\" he says."
print(food_2)   # Python's favorite food is perl
print(say_2)    # "Python is very easy." he says.


### 여러 줄인 문자열을 변수에 대입하고 싶을 때

# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline_1 = "Life is too short\nYou need python"
print(multiline_1)  # Life is too short
                    # You need python

# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline_2 = '''
Life is too short
You need python
'''
print(multiline_2)  # Life is too short
                    # You need python

multiline_3 = """
Life is too short
You need python
"""
print(multiline_3)  # Life is too short
                    # You need python

# 이스케이프 코드
"""
자주 사용
\n : 문자열 안에서 줄을 바꿀 때 사용 *
\t : 문자열 사이에 탭 간격을 줄 때 사용 *
\\ : \를 그래도 표현할 때 사용 *
\' : 작은따옴표(')를 그대로 표현할 때 사용 *
\" : 큰따옴표(")를 그대로 표현할 때 사용 *

잘 사용하지 않음
\r : 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f : 폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a : 벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b : 백 스페이스
\000 : 널 문자
"""


### 문자열 연산하기

# 1. 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)  # Python is fun!

# 2. 문자열 곱하기
a = "python"
print(a * 2)        # pythonpython

# 3. 문자열 곱하기를 응용하기
print("=" * 50)     # ==================================================
print("My Program") # My Program
print("=" * 50)     # ==================================================

# 4. 문자열 길이 구하기
a_1 = "Life is too short"
print(len(a_1))     # 17


## 1분 코딩
# 'You need python' 라는 문장을 문자열로 만들고 길이를 구해 보자.
one_minute = "You need python"
print(len(one_minute))  # 15


### 문자열 인덱싱과 슬라이싱

# 1. 문자열 인덱싱
indexing_a = "Life is too short, You need Python"
print(indexing_a[3])    # e

# indexing_a[0] = L
# indexing_a[1] = i
# indexing_a[2] = f
# indexing_a[3] = e

# 2. 문자열 인덱싱 활용하기

print(indexing_a[0])    # L
print(indexing_a[12])   # s
print(indexing_a[-1])   # n
print(indexing_a[-0])   # L
print(indexing_a[-2])   # o
print(indexing_a[-5])   # y

# 3. 문자열 슬라이싱
slicing_a = "Life is too short, You need Python"
slicing_b = slicing_a[0] + slicing_a[1] + slicing_a[2] + slicing_a[3]
print(slicing_b)        # Life
print(slicing_a[0:4])   # Life
print(slicing_a[0:3])   # Lif

# 4. 문자열을 슬라이싱하는 방법
print(slicing_a[0:5])   # Life
print(slicing_a[0:2])   # Li
print(slicing_a[5:7])   # is
print(slicing_a[12:17]) # short

print(slicing_a[19:])   # You need Python

print(slicing_a[:17])   # Life is too short

print(slicing_a[:])     # Life is too short, You need Python

print(slicing_a[19:-7]) # You need

# 5. 슬라이싱으로 문자열 나누기
slicing_c = "20260310Sunny"
date = slicing_c[:8]
weather = slicing_c[8:]
print(date)             # 20260310
print(weather)          # Sunny

year = slicing_c[:4]
day = slicing_c[4:8]
weather = slicing_c[8:]

print(year)             # 2026
print(day)              # 0310
print(weather)          # Sunny

# 6. Pithon 문자열을 Python으로 바꾸려면?
pithon = "Pithon"
print(pithon[1])        # i

print(pithon[:1])       # P
print(pithon[2:])       # thon
print(pithon[:1] + 'y' + pithon[2:])    # Python


### 문자열 포매팅이란? ###

# 문자열 포매팅 따라 하기

# 1. 숫자 바로 대입
formatting_a = "I eat %d apples." % 3
print(formatting_a) # I eat 3 apples.

# 2. 문자열 바로 대입
formatting_b = "I eat %s apples." % "five"
print(formatting_b) # I eat five apples.

# 3. 숫자 값을 나타내는 변수로 대입
number = 6
formatting_c = "I eat %d apples." % number
print(formatting_c) # I eat 6 apples.

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
formatting_d = "I ate %d apples. so I was sick for %s days." % (number, day)
print(formatting_d) # I ate 10 apples. so I was sick for three days.

# 문자열 포맷 코드
"""
%s : 문자열
%c : 문자 1개
%d : 정수
%f : 부동소수
%o : 8진수
%x : 16진수
%% : literal %(문자 % 자체)
"""

formatting_e = "I have %s apples" % 3
print(formatting_e) # I have 3 apples
formatting_f = "rate is %s" % 3.234
print(formatting_f) # rate is 3.234

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
formatting_g = "Error is %d%%." % 98
print(formatting_g) # Error is 98%.


# 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백
format_a_1 = "%10s" % "hi"
print(format_a_1)   #         hi

format_a_2 = "%-10sjane." % 'hi'
print(format_a_2)   # hi        jane.

# 2. 소수점 표현하기
format_b_1 = "%0.4f" % 3.42134234
print(format_b_1)   # 3.4213

format_b_2 = "%10.4f" % 3.42134234
print(format_b_2)   #     3.4213


# format 함수를 사용한 포매팅

# 1. 숫자 바로 대입하기
format_c_1 = "I eat {0} apples".format(3)
print(format_c_1)   # I eat 3 apples

# 2. 문자열 바로 대입하기
format_c_2 = "I eat {0} apples".format("five")
print(format_c_2)   # I eat five apples

# 3. 숫자 값을 가진 변수로 대입하기
format_c_3_number = 3
format_c_3 = "I eat {0} apples".format(format_c_3_number)
print(format_c_3)   # I eat 3 apples

# 4. 2개 이상의 값 넣기
format_c_4_number = 10
format_c_4_day = "three"
format_c_4 = "I ate {0} apples. so I was sick for {1} days.".format(format_c_4_number, format_c_4_day)
print(format_c_4)   # I ate 10 apples. so I was sick for three days.

# 5. 이름으로 넣기
format_c_5 = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(format_c_5)   # I ate 10 apples. so I was sick for 3 days.

# 6. 인덱스와 이름을 혼용해서 넣기
format_c_6 = "I ate {0} apples. so I was sick for {day} days.".format(11, day=3)
print(format_c_6)   # I ate 11 apples. so I was sick for 3 days.

# 7. 왼쪽 정렬
format_c_7 = "{0:<10}".format("hi")
print(format_c_7)   # hi        

# 8. 오른쪽 정렬
format_c_8 = "{0:>10}".format("hi")
print(format_c_8)   #         hi

# 9. 가운데 정렬
format_c_9 = "{0:^10}".format("hi")
print(format_c_9)   #     hi    

# 10. 공백 채우기
format_c_10 = "{0:=^10}".format("hi")
print(format_c_10)  # ====hi====

format_c_10_1 = "{0:!<10}".format("hi")
print(format_c_10_1)    # hi!!!!!!!!

# 11. 소수점 표현하기
format_c_11_y = 3.42134234
format_c_11 = "{0:0.4f}".format(format_c_11_y)
print(format_c_11)      # 3.4213

format_c_11_1 = "{0:10.4f}".format(format_c_11_y)
print(format_c_11_1)    #     3.4213

# 12. { 또는 } 문자 표현하기
format_c_12 = "{{ and }}".format()
print(format_c_12)      # { and }


### f 문자열 포매팅
format_d_1_name = "홍길동"
format_d_1_age = 30
print(f"나의 이름은 {format_d_1_name}입니다. 나이는 {format_d_1_age}입니다.")   # 나의 이름은 홍길동입니다. 나이는 30입니다.
print(f"저는 내년이면 {format_d_1_age + 1}살이 됩니다.")    # 저는 내년이면 31살이 됩니다.

format_d_1_d = {"name" : "홍길동", "age" : 30}
print(f"나의 이름은 {format_d_1_d["name"]}입니다. 나이는 {format_d_1_d["age"]}입니다.") # 나의 이름은 홍길동입니다. 나이는 30입니다.

print(f"{"hi":<10}")    # hi        
print(f"{"hi":>10}")    #         hi
print(f"{"hi":^10}")    #     hi    

print(f"{"hi":=^10}")   # ====hi====
print(f"{"hi":!<10}")   # hi!!!!!!!!

format_d_1_y = 3.42134234
print(f"{format_d_1_y:0.4f}")   # 3.4213
print(f"{format_d_1_y:10.4f}")  #     3.4213

print(f"{{ and }}") # { and }


## 1분 코딩
# format 함수 또는 f문자열 포매팅을 사용해 !!!python!!! 문자열을 출력해 보자.
print(f"{"python":!^12}")   # !!!python!!!
print("{0:!^12}".format("python"))  # !!!python!!!


### 문자열 관련 함수들

# 1. 문자 개수 세기 - count
strings_1_a = "hobby"
print(strings_1_a.count("b"))   # 2

# 2. 위치 알려 주기 1 - find
strings_2_a = "Python is the best choice"
print(strings_2_a.find("b"))    # 14
print(strings_2_a.find("k"))    # -1

# 3. 위치 알려 주기 2 - index
strings_3_a = "Life is too short"
print(strings_3_a.index("t"))   # 8
# print(strings_3_a.index("k"))     # error

# 4. 문자열 삽입 - join
print(",".join("abcd")) # a,b,c,d
print(",".join(['a', 'b', 'c', 'd']))   # a,b,c,d

# 5. 소문자를 대문자로 바꾸기 - upper
strings_4_a = "hi"
print(strings_4_a)          # hi
print(strings_4_a.upper())  # HI

# 6. 대문자를 소문자로 바꾸기 - lower
strings_5_a = "HI"
print(strings_5_a)          # HI
print(strings_5_a.lower())  # hi

# 7. 왼쪽 공백 지우기 - lstrip
strings_6_a = " hi "
print(strings_6_a)          #  hi
print(strings_6_a.lstrip()) # hi 

# 8. 오른쪽 공백 지우기 - rstrip
strings_7_a = " hi "
print(strings_7_a)          #  hi 
print(strings_7_a.rstrip()) #  hi

# 9. 양쪽 공백 지우기 - strip
strings_8_a = " hi "
print(strings_8_a)          #  hi 
print(strings_8_a.strip())  # hi

# 10. 문자열 바꾸기 - replace
strings_10_a = "Life is too short"
print(strings_10_a)                             # Life is too short
print(strings_10_a.replace("Life", "Your leg")) # Your leg is too short

# 11. 문자열 나누기 - split
strings_11_a = "Life is too short"
print(strings_11_a.split())         # ['Life', 'is', 'too', 'short']
strings_11_b = "a:b:c:d"
print(strings_11_b.split(':'))      # ['a', 'b', 'c', 'd']