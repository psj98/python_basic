# 파이썬 클래스

# 251번
# 클래스란, 객체를 만들기 위한 틀
# 객체란, 클래스를 기반으로 생성된 것
# 인스턴스란, 클래스로 만든 객체

# 252번
class Human:
    pass

# 253번
areum = Human()

# 254번
class Human:
    def __init__(self):
        print("응애응애")

# 255번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

# 256번
print(f'이름 : {areum.name}, 나이 : {areum.age}, 성별 : {areum.sex}')

# 257번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}')

# 258번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

# 259번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('나의 죽음을 알리지 말라')

    def who(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

# 260번
# 예약어인 print로 메서드를 정의했기 때문에 오류가 발생할 수 있음
# OMG.print()로 호출해야 함