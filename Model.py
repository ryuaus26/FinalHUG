import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/ryuaus26/Desktop/Desktop - Austin’s MacBook Air/AP CSA/world_population.csv')

by_continent = df.groupby('Continent').sum().sort_values(by='2022 Population', ascending=True)

x = by_continent.index
years = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'darkred']

fig, ax = plt.subplots(figsize=(12, 8))

for year, color in zip(years, colors):
    ax.plot(x, by_continent[str(year) + ' Population'], marker='o', linestyle='-', color=color, label=str(year))

ax.set_title('Continent Population Growth (1970 to 2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Continents', fontsize=14)
ax.set_ylabel('Population in Billions', fontsize=14)
ax.tick_params(axis='x', which='major', labelsize=12)
ax.tick_params(axis='y', which='major', labelsize=12)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend(title='Year', title_fontsize=14, fontsize=12, loc='upper left', frameon=True, fancybox=True, shadow=True)

plt.tight_layout()
plt.show()

top_pop = df.sort_values(by = '2022 Population', ascending = False).head(10)
top_pop[['Country/Territory', '2022 Population']]

countries = top_pop['Country/Territory']
populations = top_pop['2022 Population']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
bar_positions = np.arange(len(countries))

bars = ax.bar(bar_positions, populations, bar_width, color=colors, edgecolor='black', linewidth=2, alpha=0.7)

ax.set_title('Top 10 Countries with Highest Population as of 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Countries', fontsize=14)
ax.set_ylabel('Populations', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(countries, rotation=90, fontsize=12)
ax.tick_params(axis='y', labelsize=12)

# Add text annotations for population values
for bar, pop in zip(bars, populations):
    height = bar.get_height()
    ax.annotate(
        f'{int(pop):,}',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=8,
        fontweight='bold'
    )

plt.tight_layout()
plt.show()