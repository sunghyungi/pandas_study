import pandas as pd

print("# 데이터셋 가져오기")
df = pd.read_excel('./주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

print("# 연, 월, 일 데이터 분리하기")
df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head(), '\n')

print("# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기")
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())