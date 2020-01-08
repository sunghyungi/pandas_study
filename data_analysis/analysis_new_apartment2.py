import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

pd.set_option('display.max_columns', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)


# 파일 불러오기
df_2015_2019 = pd.read_csv('전국 전체 분양가격(2015_2019).csv', encoding='utf-8')
print(df_2015_2019.shape, '\n', df_2015_2019.head(), '\n', df_2015_2019.tail())

df_2013_2015 = pd.read_csv('전국 평균 분양가격(2013.09_2015.09).csv', encoding='euc-kr',
                           skiprows=1, header=0, engine='python')

print(df_2013_2015.shape, '\n', df_2013_2015.head(), '\n', df_2013_2015.tail())

print(df_2013_2015.columns)

# 24열 이후 삭제(통계정보)
df_2013_2015 = df_2013_2015.drop(columns=df_2013_2015.columns[24:])
print(df_2013_2015.columns)

year = df_2013_2015.iloc[0]
year = year.fillna(method='ffill')

month = df_2013_2015.iloc[1]
print(year, '\n', month)

for i, y in enumerate(year):
    if i > 1:
        year[i] = ' '.join([str(year[i]), '{:,.0f}'.format(month[i])])
year[1] = '시군구'

print(year)

df_2013_2015.columns = year
print(df_2013_2015)

# 통계정보 제거
df_2013_2015 = df_2013_2015.drop(df_2013_2015.index[[0, 1, 2, 10, 12, 22]])
print(df_2013_2015)

df_2013_2015.loc[4, '구분'] = ''
df_2013_2015.loc[14, '구분'] = ''
print(df_2013_2015)

# 지역 컬럼을 새로 만들어 시도와 시군구를 병합
# 결측치 빈문자로
df_2013_2015['구분'] = df_2013_2015['구분'].fillna('')
df_2013_2015.시군구 = df_2013_2015.시군구.fillna('')
print(df_2013_2015)
df_2013_2015['지역명'] = df_2013_2015.구분 + df_2013_2015.시군구

print(df_2013_2015)
print(df_2013_2015.drop(['구분', '시군구'], axis=1))
df_2013_2015 = df_2013_2015.drop(['구분', '시군구'], axis=1)

print("df_2013_2015", df_2013_2015, '\n')
melt_columns = df_2013_2015.columns.copy()
print(melt_columns, type(melt_columns))

melt_columns = melt_columns[:len(melt_columns) - 1].tolist()
print("melt_columns", '\n', melt_columns)

df_2013_2015 = pd.melt(df_2013_2015, id_vars=['지역명'],
                       value_vars=melt_columns)

print(df_2013_2015)

df_2013_2015.columns = ['지역명', '기간', '분양가']
print(df_2013_2015.head())

df_2013_2015['연도'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[0])
df_2013_2015['월'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[1])

print(df_2013_2015.head())
print(df_2015_2019.head())

print(df_2015_2019.info(), '\n\n')

print(df_2013_2015.info(), '\n\n')
df_2013_2015.연도 = df_2013_2015.연도.astype(int)
df_2013_2015.월 = df_2013_2015.월.astype(int)
print(df_2013_2015.info(), '\n\n')

plt.figure(figsize=(18, 10))
plt.subplot(221)
sns.boxplot(data=df_2013_2015, x='지역명', y='분양가', hue='연도')

plt.subplot(222)
sns.barplot(data=df_2013_2015, x='지역명', y='분양가', hue='연도')

plt.subplot(223)
sns.boxplot(data=df_2015_2019, x='지역명', y='평당분양가격', hue='연도')

plt.subplot(224)
sns.barplot(data=df_2015_2019, x='지역명', y='평당분양가격', hue='연도')
plt.suptitle("2013-2015, 2015-2019년 지역별 평당분양가격", size=20)
# plt.show()

print(df_2013_2015.columns, '\n\n', df_2015_2019.columns, '\n\n')

df_2013_2015_prepare = df_2013_2015[['지역명', '연도', '월', '분양가']]
total_columns = ['지역명', '연도', '월', '평당분양가격']
df_2013_2015_prepare.columns = total_columns

df_2015_2019_prepare = df_2015_2019[['지역명', '연도', '월', '평당분양가격']]

print(df_2013_2015_prepare.head(), '\n\n', df_2015_2019_prepare.head())
print(df_2013_2015_prepare.shape, '\n\n', df_2015_2019_prepare.shape)

df_2013_2019 = pd.concat([df_2013_2015_prepare, df_2015_2019_prepare])
print("total : ", df_2013_2019.shape)

df_year_mean = df_2013_2019.groupby(['연도'])['평당분양가격'].mean()
print(df_year_mean)

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.5, hspace=0.5)
l
df_year_mean.plot.bar(rot=0, ax=ax1)
sns.barplot(data=df_2013_2019, x='연도', y='평당분양가격', ax=ax2)
df_2013_2019[['연도', '지역명', '평당분양가격']].boxplot(by=['연도'], ax=ax3)
df_2013_2019_daegu = df_2013_2019.loc[df_2013_2019.지역명 == '대구']
sns.boxplot(x='연도', y='평당분양가격', data=df_2013_2019_daegu, ax=ax4)

ax1.set_title('연도별 평균 평당분양가격 - bar')
ax2.set_title('연도별 평균 평당분양가격 - bar')
ax3.set_title('연도별 평균 평당분양가격 - bar')
ax4.set_title('연도별 평균 평당분양가격 - bar')
fig.suptitle('연도별 평균 평당분양가격')

plt.show()