import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

print("# 집계 : 각 그룹별 요약 통계정보를 집계")
agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped, '\n')


def z_score(x):
    return (x - x.mean()) / x.std()


age_zscore = grouped.age.apply(z_score)
print(age_zscore.head(), '\n')

print("# 필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력")
age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter, '\n')
for x in age_filter.index:
    if age_filter[x]==True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head(), '\n')