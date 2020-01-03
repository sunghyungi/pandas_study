import seaborn as sns

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터 프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())
print()

print("# 사용자 함수 정의")


def add_10(n):
    return n + 10


def add_two_obj(a, b):
    return a + b


print(add_10(10))
print(add_two_obj(10, 10))
print()

print("# 시리즈 객체에 적용")
sr1 = df['age'].apply(add_10)
print(sr1.head())
print()

print("# 시리즈 객체와 숫자에 적용 : 2개의 인수(시리즈 + 숫자)")
sr2 = df['age'].apply(add_two_obj, b = 10)
print(sr2.head())
print()

print("# 람다 함수 활용 : 시리즈 객체에 적용")
sr3 = df['age'].apply(lambda x: add_10(x))
print(sr3.head())