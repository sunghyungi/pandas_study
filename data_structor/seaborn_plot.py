import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.stripplot(x="class",
              y="age",
              data=titanic,
              ax=ax1)

sns.swarmplot(x="class",
              y="age",
              data=titanic,
              ax=ax2)

ax1.set_title("Strip Plot")
ax2.set_title("Swarm Plot")

plt.show()