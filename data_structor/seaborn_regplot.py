import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.regplot(x='age',
            y='fare',
            data=titanic,
            ax=ax1)

# 그래프 그리기
sns.regplot(x='age',
            y='fare',
            data=titanic,
            fit_reg=False)

plt.show()