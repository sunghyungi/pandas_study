import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)

print("# 주식 데이터를 가져와서 데이터프레임 만들기")
df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')
print("df1", '\n')
print(df1, '\n')
print()
print('df2', '\n')
print(df2, '\n')

print("# 데이터프레임 합치기 - 교집합")
merge_inner = pd.merge(df1, df2)
print(merge_inner, '\n')

print("# 데이터프레임 합치기 - 합집합")
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer, '\n')

print("# 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리")
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(merge_left, '\n')

print("# 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리")
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right)

print(" 볼링 인덱싱과 결합하여 원하는 데이터 찾기")
price = df1[df1['price'] < 50000]
print(price.head(), '\n')

value = pd.merge(price, df2)
print(value)