import seaborn as sns
import pandas as pd
import numpy as np

titanic = sns.load_dataset('titanic')
print(titanic.head())
print()

desired_width = 600
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)

print("# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객만 따로 추출 - 불린 인덱싱")
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())
print()

print("# isin() 메서드 활용하여 동일한 조건으로 추출")
isin_filter = titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head())