import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# matplotlib.rcParams['font.family'] = 'NanumGothicCoding'

pd.set_option('display.max_columns', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)
matplotlib.rcParams['axes.unicode_minus'] = False

# 파일 불러오기
df_2015_2019 = pd.read_csv('전국 전체 분양가격(2015_2019).csv', encoding='utf-8')
print(df_2015_2019.shape, '\n', df_2015_2019.head(), '\n', df_2015_2019.tail())

df_2013_2015 = pd.read_csv('전국 평균 분양가격(2013.09_2015.09).csv', encoding='euc-kr',
                           skiprows=1, header=0, engine='python')

print(df_2013_2015.shape, '\n', df_2013_2015.head(), '\n', df_2013_2015.tail())

print(df_2013_2015.columns)

#24열 이후 삭제(통계정보)
df_2013_2015 = df_2013_2015.drop(columns=df_2013_2015.columns[24:])
print(df_2013_2015.columns)

year = df_2013_2015.iloc[0]

month = df_2013_2015.iloc[1]
print(year, '\n', month)

for i, y in enumerate(year):
    if i > 1:
        year[i] = ''.join([str(year[1]), '{:,.0f}']).format((month[i]))

year[1] = '시군구'

print(year)

df_2013_2015.columns = year
print(df_2013_2015)

# 통계정보 제거
df_2013_2015 = df_2013_2015.drop(df_2013_2015.index[[0, 1, 2, 10, 12, 22]])
print(df_2013_2015)

df_2013_2015.loc[4, '구분'] = ''
df_2013_2015.loc[14, '구분'] =''
print(df_2013_2015)

# 지역 컬럼을 새로 만들어 시도와 시군구를 병합
# 결측치 빈문자로
df_2013_2015['구분'] = df_2013_2015['구분'].fillna('')
df_2013_2015.시군구 = df_2013_2015.시군구.fillna('')
print(df_2013_2015)
df_2013_2015['지역명'] = df_2013_2015.구분 + df_2013_2015.시군구

print(df_2013_2015)
print(df_2013_2015.drop(['구분', '시군구'], axis=1))
