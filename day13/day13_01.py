# 매직 메서드
# 파이썬의 거의 대부분은 클래스로부터 만들어진 객체다

# 모든 클래스의 공통 조상 -> object클래스
# Object를 상속받고 있다면, object의 메서드를 호출할 수 있다.

# object 상속은 생략가능
# Person() -> __init__ 호출됨
class Person(object):
    # __~~__() -> 매직 메서드
    # object에 정의되어있던 __init__() 오버라이드하고 있었음
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 객체를 출력할 때(문자열화)
        return f"이름 = {self.name}, age = {self.age}"

    def __eq__(self, other):    # == 연산 시 호출
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other

    # less than -> __ lt__ -> "<"
    # greater than -> __gt__ -> ">"
    # less than or equal -> __le__ -> "<="
    # greater than or equal -> __ge__ -> ">="
    def __lt__(self, other):    # < 연산 시 호출
        print("나이 비교")
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    # + 연산시, 나이를 더한 Person객체가 나오길 바람
    # + 연산 -> __add__()
    # - 연산 -> __sub__()
    # * 연산 -> __ mul__()
    # / 연산 -> __div__()
    def __add__(self, other):
        if isinstance(other, int):
            new_age = self.age + other
            name = self.name
            # 제 3의 객체를 리턴
            return Person(name, new_age)


p1 = Person("홍길동", 20)
p2 = Person("김길동", 20)
print(p1 == p2)
print(p1 < 30)
p3 = p1 + 5
print(p3)   # 리턴받은 제 3의 객체
print(p1)

# 좌표 클래스
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 같은 Coord 객체끼리
    # == 연산 시 x, y좌표 동일하면 true
    def __eq__(self, other):
        if isinstance(other, Coord):
            is_same_x = self.x == other.x
            is_same_y = self.y == other.y
            return is_same_x and is_same_y
    # + 연산 시, x좌표 y좌표가 각각 더해지게
    def __add_(self, other):
        if isinstance(other, Coord):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Coord(new_x, new_y)
    # - 연산 시, x좌표 y좌표가 각각 빼지도록
    def __sub_(self, other):
        if isinstance(other, Coord):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Coord(new_x, new_y)
    # 객체 출력 시, "현재좌표 : ({x좌표}, {y좌표})"
    def __str__(self):
        Coord_str = (f"현재 좌료 : :({self.x}, {self.y})")

c1 = Coord(1,2)
print(c1)

c1 = Coord(1, 2)
c2 = Coord(1, 2)
c3 = Coord(2, 4)
print(c1 ==2)
print(c1 == c3)
print(c1 ==2)
print("hi:" *50)
print(c1 ==2)