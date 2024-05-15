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
years = [1970 ,1980 ,1990 ,2000 ,2010 ,2015 ,2020 , 2025, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140]

# Predict the population for future years
future_population = []
for year in years:
    predicted_population = slope * year + intercept
    future_population.append({'year': year, 'total_population': predicted_population})

# Convert the list of dictionaries to a DataFrame
future_population_df = pd.DataFrame(future_population)

# Create the line plot with circle data points
fig = px.line(markers = True,data_frame = future_population_df, x='year', y='total_population', title='Total World Population (with Future Prediction) <br> Regression Model y =m(x) + b')
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Population',
    xaxis_range=[1970, 2150],  # Adjust the x-axis range to include future years
    yaxis_range=[0, future_population_df['total_population'].max() * 1.1]  # Adjust the y-axis range to include future values
)

# Display the plot
fig.show()

import pandas as pd
import numpy as np
from plotly.graph_objs import go, frames
from plotly.offline import iplot

# ... (your existing code for data loading and prediction)

# Define empty lists for traces and layout updates
traces = []
layout_updates = []

# Function to create a trace for a single year
def create_trace(year, population):
    return go.Scatter(
        x=[year],
        y=[population],
        mode='markers',
        marker=dict(size=10, color='blue')
    )

# Create traces for initial years (e.g., first 5 years)
for i in range(5):
    year = years[i]
    population = future_population_df.loc[i, 'total_population']
    traces.append(create_trace(year, population))

# Function to update layout based on current data
def update_layout(current_year):
    x_range = [1970, current_year + 1]
    y_range = [0, future_population_df['total_population'].max() * 1.1]
    return {'xaxis.range': x_range, 'yaxis.range': y_range}

# Create layout updates for initial years
for i in range(5):
    year = years[i]
    layout_updates.append(update_layout(year))

# Define frames and animation layout
frames_data = [go.Frame(data=traces, layout=)]
layout = go.Layout(
    title='Total World Population (Animated Prediction) <br> Regression Model y =m(x) + b',
    xaxis_title='Year',
    yaxis_title='Population'
)

# Animation configuration (adjust speed as needed)
animation = go.layout.Animate(
    transition={'duration': 500},  # milliseconds per frame transition
    frame_order='auto',
    frames=frames_data
)

# Combine everything into a figure object
fig = go.Figure(data=traces, layout=layout)
fig.update_layout(updatemenus=[go.layout.Updatemenu(
    buttons=[go.buttons.Button(label="Play", method="animate", args=[None])])])
fig.update_layout(animations=[animation])

iplot(fig)