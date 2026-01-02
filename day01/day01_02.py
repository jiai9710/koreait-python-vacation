# str의 기능들
my_str = "Hello, world!"

# 문자열 길이 - len(문자열데이터)
my_str_length = len(my_str)
print(my_str_length) # 13

# 문자열 슬라이싱 (중요)
# 문자열데이터[시작번호:끝번호]
# 시작번호 이상 ~ 끝번호 미만(쉼표까지 나오게 할려면 6번, 즉 7번째까지 입력해야함)
print(my_str[0:5])
print(my_str[:5])   # 0은 생략가능
print(my_str[7:13]) # 뒤를 생략하면 끝까지라는 의미

# 실습) ssn에 담긴 주민번호의 뒷자리를 "*"로 바꾸어주세요
# 991111-1234567 -> 991111-******* 출력해보기
ssn = "991111-1234567"
ssn[:7]
print(ssn[:7] + "*" * 7)    # 문자열의 곱셈이 가능함. ("*" * 7 = "*******")


# find() : 해당문자의 위치(index) 가져온다
# 만약에 해당문자가 없으면 -1을 가져옴(맨 마지막)
# index() : 해당문자의 위치(index) 가져온다
# 만약에 해당문자가 없으면 에러 발생
index_of_dash = ssn.find("-")


# 같은 답 (더 좋은 답이긴 함)
# 뒷자리 문자 갯수
ssn = "991111-1234567"
length_last_ssn = len(ssn[7:])
print(ssn[:7] + "*" * 7)

# 해당문자의 위치 찾아서 끊은 버전
ssn = "991111-1234567"
length_last_ssn = len(ssn[index_of_dash + 1:])  # 더 좋은 코드임
print(ssn[:7] + "*" * 7)

# 주민번호 앞자리
first_ssn = ssn[:index_of_dash + 1]

print(first_ssn + "*" * length_last_ssn)

# "-" 위치 기준으로 코드를 짰기 때문에 앞 뒤 문자 개수가 늘어나도 "-" 인덱스 번호를 세지 않아도 쉽게 끊을 수 있음

# 실습) 이메일 데이터에서 아이디만 추출
# 조건) 아이디가 바뀌더라도, 아이디가 추출되어야 합니다.
email = "python@py.com"
index_of_email = email.find("@")
username = email[:index_of_email]

print(username)