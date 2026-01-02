#day03_01.py
"""
멀티라인 - 함수설명(dicString)용
변수에 할당하지만 않으면, 주석처럼 사용가능 (Enter키를 포함한 문자열을 출력할 때도 사용)
"""

name = "홍길동"
test = """hello # Enter도 출력됨
world!
my name is {name}
"""
print(test)

"""
조건문
if bool데이터:
    bool데이터가 True일때 실행되는 코드
"""
# 코드블럭 - 코드의 영역
# 들여쓴 부분을 하나의 코드블럭으로 간주한다.
if False:
    print("if문 안쪽입니다.")
print("if문 밖입니다.")

# 10만원 이상이면 10% 할인가격
# 아니면 할인이 없는 가격
# input()으로 받아온 데이터를 모두 str이다. -> 문자열이기때문에 형변환이 필요함
# price = input("상품가격을 입력하세요 >>")
# price = int(price)
#
# price = int(input("상품가격을 입력하세요 >>"))
#
# if price >= 100000:
#     price = price * 0.9 # -> price *= 0.9
#     print(price)
# else:   # 위의 모든 조건이 False일 때
#     print(price)
#
# # if ~ elif ~ else : 하나의 코드블럭만 샐행
# #순차적으로 검사(위
#
# age = 15
# if age >= 20:
#     print("성인")
# if age >= 17:
#     print("고등학생")
# if age >= 14:
#     print("성인")
# if age >= 8:
#     print("미취학아동")

"""bmi 계산기
bmi = 체중(kg) / 키(m) * 키(m)
bmi가 30이상 비만 / 25이상 30미만 과체중
18.5d이상 25미만 정상 / 18.5미만 저체중
철수(174cm, 70kg)으 비만도를 출력"""

weight = 70
height = 174 / 100
bmi = weight / (height ** 2) # 제곱

if bmi >= 30:
    print("비만")
if bmi >= 25:   # 위의 조건들이 False -> bmi < 30
    print("과체중")
if bmi >= 18.5:
    print("정상")
if bmi < 18.5:  # bmi < 30 and bmi < 25
    print("저체중")

# 홀짝 판별
# num이라는 변수에 숫자를 입력받고
# 짝수면 짝수입니다. 홀수면 홀수입니다. 출력

num = input("숫자를 입력해주세요 >> ")
num = int(num)  # input으로 데이터 받게 되면 문자열(str)로 받게됨
# 따라서 str -> int 형변환
isEven = num % 2 == 0

if isEven == 0:
    print("짝수입니다.")
if isEven == 1: # else 써도 됨
    print("홀수입니다.")