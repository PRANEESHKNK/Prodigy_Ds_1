
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram of Population Distribution in 2020
plt.figure(figsize=(6, 4))
sns.histplot(df['2020'], kde=False, bins=20)
plt.title('Population Distribution in 2020')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()

# Barplot for All Countries
plt.figure(figsize=(40, 12)) 
sns.barplot(x='Country Name', y='2020', data=df)
plt.title('Population Distribution in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=90)
plt.show()

# Top 10 Countries by Population in 2020
top10 = df.sort_values(by='2020', ascending=False).head(10)
plt.figure(figsize=(20, 8))
sns.barplot(x='Country Name', y='2020', data=top10)
plt.title('Top 10 Countries with Highest Population in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

# Bottom 10 Countries by Population in 2020
least10 = df.sort_values(by='2020', ascending=True).head(10)
plt.figure(figsize=(20, 8))
sns.barplot(x='Country Name', y='2020', data=least10)
plt.title('Bottom 10 Countries with Lowest Population in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()
