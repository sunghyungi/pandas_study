import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

for key, group in grouped:
    print("* key : ", key)
    print("* number : ", len(group))
    print("age(mean) : ", group.age.mean())
    print()

print("# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임으로 반환")
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head(), '\n', type(grouped_filter), '\n')

print(grouped_filter['class'].value_counts())

print("# age 열의 평균이 30보다 작은 그룹만ㅇ르 필터링하여 데이터프레임으로 반환")
age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail(), '\n', type(age_filter), '\n', age_filter['class'].value_counts())