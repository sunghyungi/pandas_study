import seaborn as sns

print("# titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
print(df, '\n')

print("# 열 이름의 리스트 만들기")
columns = list(df.columns.values)
print(columns, '\n')

print("# 열 이름을 알파벳 순으로 정렬하기")
columns_sorted = sorted(columns)
df_sorted = df[columns_sorted]
print(df_sorted, '\n')

print("# 열 이름을 기존 순서의 정반대 역순으로 정렬하기")
columns_reversed = list(sorted(columns, reverse=True))
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

print("# 열 이름을 사용자가 정의한 임의의 순서로 재배치하기")
columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = df[columns_customed]
print(df_customed)