import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px

# Load data
df = pd.read_csv('world_population.csv')

# Create a list of population columns
population_columns = [col for col in df.columns if col.endswith('Population')]

# Create a new DataFrame with the total population for each year
total_population = df[population_columns].sum().reset_index()
total_population.columns = ['year', 'total_population']

# Convert the year column to numeric
total_population['year'] = total_population['year'].str.replace(' Population', '').astype(int)

# Calculate the regression coefficients
fit = np.polyfit(total_population["year"], total_population["total_population"], deg=1)
slope, intercept = fit

# Define the years for prediction
years = [1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070, 2075, 2080, 2085, 2090, 2095, 2100, 2105, 2110, 2115, 2120, 2125, 2130, 2135, 2140]


# Predict the population for future years
future_population = []
for year in years:
    predicted_population = slope * year + intercept
    future_population.append({'year': year, 'total_population': predicted_population})

# Convert the list of dictionaries to a DataFrame
future_population_df = pd.DataFrame(future_population)

# Create the line plot with circle data points
fig = px.line(markers = True,future_population_df, x='year', y='total_population', title='Total World Population (with Future Prediction) <br> AI Model y =m(x) + b')
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Population',
    xaxis_range=[1970, 2150],  # Adjust the x-axis range to include future years
    yaxis_range=[0, future_population_df['total_population'].max() * 1.1]  # Adjust the y-axis range to include future values
)

# Display the plot
fig.show()