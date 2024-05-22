import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px

# Load data
df = pd.read_csv('world_population.csv')

# Calculate arithmetic density
df['Arithmetic Density'] = df['2022 Population'] / df['Area (km²)']

# Create choropleth map
fig = px.choropleth(df, locations='Country/Territory',
                    color='Arithmetic Density',
                    hover_name='Country/Territory',
                    color_continuous_scale='jet',
                    scope= "south america",
                    projection = "equirectangular",
                    locationmode='country names',
                    range_color=(0, 50))  # Set the range for the color scale

# Customize layout
fig.update_layout(
    title=dict(text='<b>Countries Arithmetic Density (2022) <br> Arithematic Density = Population / Area of land km^2 </b>', x=0.5),
    coloraxis_colorbar=dict(
        title='Arithmetic Density',
        tickprefix='',
        len=0.8
    )
)

# Display the choropleth map
fig.show()