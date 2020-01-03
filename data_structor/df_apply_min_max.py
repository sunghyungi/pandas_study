import seaborn as sns

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()).
print()


# 사용자 함수 정의
def min_max(x):
    return x.max() - x.min()


print("# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환")
result = df.apply(min_max)
print(result, type(result), sep='\n')


def add_two_obj(a, b):
    return a + b


print("# 데이터프레임의 2개 열을 선택하여 적용")
print("# x=df, a=df['age'], b=df['ten']")
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)