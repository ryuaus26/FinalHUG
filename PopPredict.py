import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('world_population.csv')

# Create a list of population columns
population_columns = [col for col in df.columns if col.endswith('Population')]

# Create a new DataFrame with the total population for each year
total_population = df[population_columns].sum().reset_index()
total_population.columns = ['year', 'total_population']

# Convert the year column to numeric
total_population['year'] = total_population['year'].str.replace(' Population', '').astype(int)

# Plot the total population
fig = px.line(total_population, x='year', y='total_population', title='Total World Population <br> Regression Model: y = (8.33710451 * 10^7 * x) -1.60587660*10^11 <br> x: years')
fig.update_xaxes(title_text='Year')
fig.update_yaxes(title_text='Population')

fig.show()


fit = np.polyfit(total_population["year"], total_population["total_population"],deg = 1)

#y = (8.33710451 * 10^7 * x) -1.60587660*10^11

#Years to predict
years = []