import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("df['horsepower']", '\n', df['horsepower'], '\n')

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print("# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers, '\n')

# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels=bin_names,
                      include_lowest=True)

print("# horsepower 열, hp_bin 열의 첫 15행을 출력")
print(df[['horsepower', 'hp_bin']].head(15), '\n')

print(df['hp_bin'].cat.categories)