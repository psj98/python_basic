# 파이썬 클래스

# 271번
import random

class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

# 272번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

# 273번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

# 274번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

    def deposit(self, price):
        if price >= 1:
            self.balance += price

# 275번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

    def deposit(self, price):
        if price >= 1:
            self.balance += price

    def withdraw(self, price):
        if price < self.balance:
            self.balance -= price

# 276번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

    def deposit(self, price):
        if price >= 1:
            self.balance += price

    def withdraw(self, price):
        if price < self.balance:
            self.balance -= price

    def display_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.accountNum}')
        print('잔고 : ' + format(self.balance, ','))

# 277번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        self.depositCount = 0

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

    def deposit(self, price):
        if price >= 1:
            self.balance += price
            self.depositCount += 1
            if self.depositCount % 5 == 0:
                self.balance *= 1.01

    def withdraw(self, price):
        if price < self.balance:
            self.balance -= price

    def display_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.accountNum}')
        print('잔고 : ' + format(self.balance, ','))

# 278번
data = []

k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)

data.append(k)
data.append(l)
data.append(p)

# 279번
for i in data:
    if i.balance >= 1000000:
        i.display_info()

# 280번
class Account():
    accountCount = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        self.depositCount = 0
        self.depositHis = []
        self.withdrawHis = []

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accountNum = num1 + '-' + num2 + '-' + num3

        Account.accountCount += 1

    def get_account_num(self):
        print(self.accountCount)

    def deposit(self, price):
        if price >= 1:
            self.balance += price
            self.depositHis.append(price)
            self.depositCount += 1
            if self.depositCount % 5 == 0:
                self.balance *= 1.01

    def withdraw(self, price):
        if price < self.balance:
            self.withdrawHis.append(price)
            self.balance -= price

    def display_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.accountNum}')
        print('잔고 : ' + format(self.balance, ','))

    def deposit_history(self):
        for i in self.depositHis:
            print(i)

    def withdraw_history(self):
        for i in self.withdrawHis:
            print(i)