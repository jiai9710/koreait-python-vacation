# 연산자

# 산술연산자(사칙연산)
print(20 + 20)
print(20 - 20)
print(20 * 20)
print(20 / 8)  # 소숫점 표현 : 2.xx
print(20 // 8) # 몫 : 2
print(20 % 8) # 나머지 : 4
print(2**4) # 2의 4승

print("홍" + "길동")   # "홍길동"
# print("홍" + 3)  # "홍홍홍"

num = 108
# num이 2의 배수인가요? = 짝수인가요?
print(num % 2 == 0)
# num이 2의 배수가 아닌가요? = 홀수인가요?
print(num % 2 == 1) # or print(num % 2 != 0)
# num이 3의 배수인가요?
print(num % 3 == 0)

# 실습) 한페이지당 20개의 게시글을 볼 수 있음
# 게시판의 총 게시글은 162개
# 이때 총 페이지의 갯수와 마지막 페이지의 게시글 수 print 하라.
total_post = 162
total_page_count = (total_post // 20) + 1 # 나머지 2개의 게시글을 보기 위해서 한페이지를 더 추가해줘야 함
# total_post // 20 + 1 에서 사칙연산 법칙으로 나눗셈이 덧셈보다 먼저 수행하지만
# 구분하기위해서 괄호 추가해줬음 -> (total_post // 20) + 1
last_page_post_count = total_post % 20
print("총 페이지 : ", total_page_count)
print("마지막페이지 게시글 수 : ", last_page_post_count)

# 비교연산자 -> 결과가 bool형(true, false)
x = 10
y = 20
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
print(x > y)

# x > 5 and x < 20
print(5 < x < 20)

# 논리연산자
# not / or / and
a = True
b = False
print(a and b)  # and : 둘 다 True 여야 True
print(a or b)   # or : 둘 중 하나만 True 여도 True
print(not a)    # not : bool값을 반전

# 대입연산자 - 우선순위가 가장 낮음
num = 10
# 복합대입연산자
num = num + 5
num += 5    # num = num + 5
num -= 5    # num = num - 5
num *= 5    # num = num * 5
num /= 5    # num = num / 5

# 연산자 우선순위(걍 참고용)
# 괄호 () > 산술연산자 > 비교연산자 > 논리연산자 > 대입연산자 -> 괄호가 제일 높은건 알아둬야함
