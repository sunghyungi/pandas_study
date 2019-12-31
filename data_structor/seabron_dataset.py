import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 600)

print(titanic.head(), '\n', titanic.info())