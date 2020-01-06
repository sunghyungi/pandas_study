import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

print("# 각 그룹에 대한 모든 열의 표준편차를 집계하여 데이터프레임으로 반환")
std_all = grouped.std()
print(std_all, '\n', type(std_all), '\n')

print("# 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환")
std_fare = grouped.fare.std()
print(std_fare, '\n', type(std_fare), '\n')

def min_max(x):
    return x.max() - x.min()

print("# 각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계")
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head(), '\n')

print("# 여러 함수를 각 열에 동일하게 적용하여 집계")
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head(), '\n')

print("# 각 열마다 다른 함수를 적용하여 집계")
agg_sep = grouped.agg({'fare': ['min', 'max'], 'age': 'mean'})
print(agg_sep.head())