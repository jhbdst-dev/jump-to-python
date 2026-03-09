### 숫자형은 어떻게 만들고 사용할까? ###

# 정수형

int_a = 123
int_a = -178
int_a = 0


# 실수형

float_a = 1.2
float_a = 3.45

float_a = 4.24E10
float_a = 4.24e-10


# 8진수와 16진수

a = 0o177
print(a)    # -> 127

a = 0x8ff
b = 0xABC
print(b)    # -> 2748


### 숫자형을 활용하기 위한 연산자 ###

# 사칙연산

a = 3
b = 4
print(a + b)    # 7
print(a - b)    # -1
print(a * b)    # 12
print(a / b)    # 0.75


# x의 y제곱을 나타내는 ** 연산자

a = 3
b = 4
print(a ** b)   # 81


## 1분 코딩

print(10*18**2+2*11)    # 3262


# 나눗셈 후 나머지를 리턴하는 % 연산자

print(7 % 3)    # 1
print(3 % 7)    # 3


# 나눗셈 후 몫을 리턴하는 // 연산자

print(7 / 4)    # 1.75
print(7 // 4)   # 1


## 1분 코딩

print(14 // 3)  # 4
print(14 % 3)   # 2