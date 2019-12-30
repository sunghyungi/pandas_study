import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('시도별 전출입 인구수.xlsx', fillna=0, header=0)

df = df.fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

plt.style.use('ggplot')

fig = plt.figure(figsize=(16, 14))
fig.subplots_adjust(left=0.2, right=0.8, bottom=0.2, top=0.87, wspace=0.3, hspace=0.5)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울 -> 경기')
ax2.legend(loc='best')

ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

ax1.set_xlabel('기간')
ax1.set_ylabel('이동 인구수')
ax1.set_title('서울 -> 경기 인구 이동')

ax2.set_xlabel('기간')
ax2.set_ylabel('이동 인구수')
ax2.set_title('서울 -> 경기 인구 이동')

plt.show()