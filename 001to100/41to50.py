# 파이썬 문자열

# 41번
ticker = "btc_krw"
print(ticker.upper())

# 42번
ticker = "BTC_KRW"
print(ticker.lower())

# 43번
a = "hello"
print(a.capitalize())

# 44번
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 45번
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

# 46번
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 47번
a = "hello world"
b = a.split(" ")
print(b)

# 48번
ticker = "btc_krw"
ticker_split = ticker.split("_")
print(ticker_split)

# 49번
date = "2020-05-01"
date_split = date.split("-")

year = date_split[0]
month = date_split[1]
day = date_split[-1]

print(year, month, day)

# 50번
data = "039490     "
print(data.rstrip())
# lstrip()은 왼쪽 공백 제거