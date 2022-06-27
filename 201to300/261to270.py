# 파이썬 클래스

# 261번
class Stock():
    pass

# 262번
class Stock():
    def __init__(self, stockName, stockCode):
        self.stockName = stockName
        self.stockCode = stockCode

# 263번
class Stock():
    def __init__(self, stockName, stockCode):
        self.stockName = stockName
        self.stockCode = stockCode

    def set_name(self, stockName):
        self.stockName = stockName

# 264번
class Stock():
    def __init__(self, stockName, stockCode):
        self.stockName = stockName
        self.stockCode = stockCode

    def set_name(self, stockName):
        self.stockName = stockName

    def set_code(self, stockCode):
        self.stockCode = stockCode

# 265번
class Stock():
    def __init__(self, stockName, stockCode):
        self.stockName = stockName
        self.stockCode = stockCode

    def set_name(self, stockName):
        self.stockName = stockName

    def set_code(self, stockCode):
        self.stockCode = stockCode

    def get_name(self):
        return self.stockName

    def get_code(self):
        return self.stockCode

# 266번
class Stock():
    def __init__(self, stockName, stockCode, per, pbr, profit):
        self.stockName = stockName
        self.stockCode = stockCode
        self.per = per
        self.pbr = pbr
        self.profit = profit

    def set_name(self, stockName):
        self.stockName = stockName

    def set_code(self, stockCode):
        self.stockCode = stockCode

    def get_name(self):
        return self.stockName

    def get_code(self):
        return self.stockCode

# 267번
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)

# 268번
class Stock():
    def __init__(self, stockName, stockCode, per, pbr, profit):
        self.stockName = stockName
        self.stockCode = stockCode
        self.per = per
        self.pbr = pbr
        self.profit = profit

    def set_name(self, stockName):
        self.stockName = stockName

    def set_code(self, stockCode):
        self.stockCode = stockCode

    def get_name(self):
        return self.stockName

    def get_code(self):
        return self.stockCode

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, profit):
        self.profit = profit

# 269번
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
samsung.set_per(12.75)

# 270번
종목 = []

samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
hyundai = Stock('현대차', '005380', 8.70, 0.35, 4.27)
lg = Stock('LG전자', '066570', 317.34, 0.69, 1.37)

종목.append(samsung)
종목.append(hyundai)
종목.append(lg)

for i in 종목:
    print(i.stockCode, i.per)