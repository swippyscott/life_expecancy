import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Scott\Downloads\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\all_data.csv")
print(df.head())

sns.barplot(data = df, x = 'Year', y = 'Life expectancy at birth (years)')
plt.show()

plt.clf()
sns.histplot(data = df, x = 'Life expectancy at birth (years)', bins = 50)
plt.show()
