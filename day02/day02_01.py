# 문자열 기능들 - 2
from string import ascii_lowercase

# replace("바꾸고 싶은 문자열", "대체될 문자열")
a = "life is too short you need python"
a_replace = a.replace(" ","_")
print(a_replace)
a_replace = a.replace("python","")
print(a_replace)    # 삭제

# strip - 문자열 처음과 끝에서 매칭되는 문자를 삭제
a = "  특가 할인행사  "
a_strip = a.strip() # 기본으로 공백을 삭제한다.
print(a_strip)  # 좌우 공백 사라짐 (중간 공백은 남음) -> 출력 : 특가 할인행사
a = "**특가 할인행사**"
a_strip = a.strip("*")  # 매칭되는 문자 하나만 적어주기
a_rstrip = a.rstrip("*")    # 문자열 끝 부분
a_lstrip = a.lstrip("*")    # 문자열 시작 부분
print(a_strip)  # 출력 : 특가 할인행사

# upper, lower
a = "hello world"
a_upper = a.upper() # 문자열을 모두 대문자로
a_lower = a.lower() # 문자열을 모두 소문자로
print(a_upper, a_lower)

# in 연산자 (중요) - 존재 여부 확인
isHelloExist = "Hello" in a # bool타입 결과 (true/false)
print(isHelloExist)
print("world" in a) # a변수가 담은 데이터에 "world" 있나요?
print("홍" in "홍길동") # "홍길동"에 "홍"이 있나요?

# 문자열의 처음과 끝이 무엇인지 검사
# startswith(), endswith()
email = "python@py.com"
print(email.startswith("python"))   # bool타입 결과
print(email.endswith(".com"))   # bool타입 결과

name = "홍길동"
# 성씨가 홍인지 검사 -> true / false
# 2가지 방법 / a == b : a와 b가 같나요?
# 첫 번째 방법
print(name.startswith("홍"))

# 두 번째 방법
print(name[0] == "홍")

# 실습
production = "**[SALE] Apple iphone 17 pro**"
# "apple iphone 17 pro"
# strip(), replace(), lower()
production_strip = production.strip("*")

# 문자열기능들은 원본을 바꾸지 X
print("원본 : ", production)
print("가공 : ", production_strip)    # production_strip 이라는 새로운 변수에 *이 삭제된 데이터가 들어감

# ** 앞뒤 제거
production = production.strip("*")  # *이 삭제된 데이터가 production에 새로 대입됨 -> 재대입은 가능함
# [SALE] 제거
production = production.replace("[SALE]","")
# 모든 문자 소문자로
production = production.lower()

print(production)
# 기능들? -> 함수 : 특정기능들을 실행하는 단위
# 함수의 결과가 값이면 값처럼 사용이 가능하다.
production = "**[SALE] Apple iphone 17 pro**"
production = (production
              .strip("*")
              .replace("[SALE]","")
              .lower()) # 연속적으로 사용 가능
print(production)

production = (production.strip("*").replace("[SALE]","").lower()) # 일렬으로도 사용 가능
print(production)

