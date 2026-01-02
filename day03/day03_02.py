# (자료)형변환
num1 = int("11")    # str -> int
print(type(num1))
num2 = int(11.0)    # float -> int
print(type(num2))

# num5 = int("hello") -> Error

fnum1 = float(11)
print(type(fnum1))
fnum2 = float("11")
print(type(fnum2))

print(str(100) + "원")   # -> print(100+"원") => Error(숫자와 문자열은 연산할 수 없다는 에러 뜸)

# bool(): 논리값(True of False)으로 변환
print(bool("홍길동"))  # True(space bar 등의 문자가 하나라도 있으면 True 출력)
print(bool("")) # False
print(bool(0))  # False
print(bool([])) # 비어있는 list, dict, tuple -> False

# if 뒤 bool데이터자리에 다른 자료형이 오면 자동형변환
if 100:
    print("실행될까요?")
if "":
    print("실행안됩니다") # -> 출력 XX
