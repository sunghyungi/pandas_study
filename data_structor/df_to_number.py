import pandas as pd
import seaborn as sns

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 600)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(titanic.head())
print(df.head(), type(df), sep='\n')
print()

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep='\n')
