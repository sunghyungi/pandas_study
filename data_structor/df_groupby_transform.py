import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

print("# 그룹별 age 열의 표준편차 집계 연산")
age_mean = grouped.age.mean()
print(age_mean, '\n')

print("# 그룹별 age 열의 표준편차 집계 연산")
age_std = grouped.age.std()
print(age_std, '\n')

print("# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력")
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3), '\n')


def z_score(x):
    return (x - x.mean()) / x.std()

print("# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환")
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]], '\n')
print(len(age_zscore), '\n')
print(age_zscore.loc[0:9], '\n')
print(type(age_zscore))