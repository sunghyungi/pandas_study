import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']

cylinders_size = df.cylinders /df.cylinders.max() * 300

df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5), cmap='viridis', s=50, c=cylinders_size, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')

plt.savefig("./scatter.png")
plt.savefig("./scatter_transparent.png", transparent=True)
plt.show()