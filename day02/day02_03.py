# 조건 연산자(삼항 연산자)

score = 50
cut_line_score = 60
# (True일때 값) if (bool데이터) else (False일때 값)
result = "pass" if score >= cut_line_score else "fail"
print(result)

# 여러조건(중첩)
grade = 90
grade = "A" if grade >= 90 else ("B" if grade >= 80 else "C")
print(grade)

# 로그인
real_id = "python"
real_pw = "1234" # -> 1234 하면 오류 => 문자열이 아니기 때문

# input()을 통해 input_id와 input_pw 입력받아 주세요
# 입력받은 데이터와 real_id / real_pw를 비교하여
# 둘 다 같으면 "로그인 성공", 하나라도 다르면 "로그인 실패" 출력

input_id = input("아이디를 입력하세요 : ")
input_pw = input("패스워드를 입력하세요 : ")
# 만약 문자열이 아니고 그냥 숫자로 할거면
# input_pw = int(input_pw)  # (자료)형변환

#선생님 답
isSameId = input_id == real_id
isSamePw = input_pw == real_pw  # 1234 == "1234" : 에러뜨는 이유
isLogin = isSameId and isSamePw
result = "로그인 성공" if isLogin else "로그인 실패"
print(result)

# 내 풀이
login = "로그인 성공" if (input_id == real_id) and (input_pw == real_pw) else "로그인 실패"
# 자바랑 연산자 헷갈리지말기 -> python은 && 안씀 and 쓰기
print(login)

# 상품의 가격을 입력받아 10% 할인가를 출력
price = input("상품의 가격을 입력하세요 >> ")
price = int(price)
sale_price = price * 0.9
print(sale_price)
