import pandas as pd

print("# Period 배열 만들기 - 1개월 길이")
pr_m = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='M')
print(pr_m, '\n')

print("# Period 배열 만들기 - 1시간 길이")
pr_h = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='H')
print(pr_h, '\n')

print("# Period 배열 만들기 - 2시간 길이")
pr_2h = pd.period_range(start='2019-01-01',
                        end=None,
                        periods=3,
                        freq='2H')
print(pr_2h)