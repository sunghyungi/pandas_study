import pandas as pd

dict_value = {'a': 1, 'b': 2, 'c': 3}

sr = pd.Series(dict_value)

print(type(sr), sr, sep="\n")

