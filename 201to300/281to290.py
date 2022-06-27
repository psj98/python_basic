# 파이썬 클래스

# 281번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

# 282번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    pass

# 283번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
class 자전차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

# 284번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

# 285번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print(f'바퀴 수 : {self.바퀴}')
        print(f'가격 : {self.가격}')

# 286번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print(f'바퀴 수 : {self.바퀴}')
        print(f'가격 : {self.가격}')

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

# 287번
class 차():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print(f'바퀴 수 : {self.바퀴}')
        print(f'가격 : {self.가격}')

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print(f'구동계 : {self.구동계}')

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

# 288번
# 자식호출

# 289번
# 자식생성

# 290번
# 자식생성
# 부모생성