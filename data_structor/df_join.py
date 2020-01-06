import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)

df1 = pd.read_excel('./stock price.xlsx', index_col='id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id')

print("df1", '\n', df1, '\n\n')
print("df2", '\n', df2, '\n')

print("# 데이터프레임 결합(join)")
df3 = df1.join(df2)
print(df3)
print()

print("# 데이터프레임 결합(join) - 교집합")
df4 = df1.join(df2, how='inner')
print(df4)