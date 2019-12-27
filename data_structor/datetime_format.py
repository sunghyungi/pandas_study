import pandas as pd

df = pd.read_csv('stock-data.csv')

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)

print("# 문자열인 날짜 데이터를 판다스 Timestamp로 변환")
df['new_Date'] = pd.to_datetime(df['Date'])
print(df, '\n')

print("# dt속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분")
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df, '\n')

print("# Timestamp를 Period로 변환하여 년월일 표기 변경하기")
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df, '\n')

print("# 원하는 열을 새로운 행 인덱스로 지정")
df.set_index('Date_m', inplace=True)
print(df)