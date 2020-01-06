import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)

print("# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head(), '\n')

print("# 행, 열, 값, 집계에 사용할 열을 1개씩 지정 - 평균 집계")
pdf1 = pd.pivot_table(df, index='class',
                      columns='sex',
                      values='age',
                      aggfunc='mean')

print(pdf1.head(), '\n')


print("# 값에 적용하는 지계 함수를 2개 이상 지정 가능 - 생존율, 생존자 수 집계")
pdf2 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='survived',
                      aggfunc=['mean', 'sum'])

print(pdf2.head(), '\n')

print("# 행, 열, 값에 사용할 열을 2개 이상 지정 가능 - 평균 나이, 최대 요금 집계")
pdf3 = pd.pivot_table(df,
                      index=['class', 'sex'],
                      columns='survived',
                      values=['age', 'fare'],
                      aggfunc=['mean', 'max'])

pd.set_option('display.max_columns', 10)
print(pdf3.head(), '\n')


print("# 행, 열 구조 살펴보기")
print(pdf3.index)
print(pdf3.columns, '\n')

print("# xs 인덱서 사용 - 행 선택(default: axis=0)")
print(pdf3.xs('First'))
print()
print(pdf3.xs(('First', 'female')))
print()
print(pdf3.xs('male', level='sex'))
print()
print(pdf3.xs(('Second', 'male'), level=[0, 'sex']))
print()

print("# xs 인덱서 사용 - 열 선택(axis=1 설정)")
print(pdf3.xs('mean', axis=1))
print()
print(pdf3.xs(('mean', 'age'), axis=1))
print()
print(pdf3.xs(1, level='survived', axis=1))
print()
print(pdf3.xs(('max', 'fare', 0), level=[0,1,2], axis=1))