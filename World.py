import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px

# Load data
max_range = 0
wp_df = pd.read_csv('world_population.csv')
wp_df.columns = ['Rank', 'ISO-3', 'Country', 'Capital', 'Continent', '2022', '2020', '2015',
                 '2010', '2000', '1990', '1980', '1970', 'Area (km²)', 'Density (per km²)', 'Growth Rate',
                 'World Population Percentage']
wp_df = wp_df[['Rank', 'ISO-3', 'Country', 'Capital', 'Continent', 'Area (km²)', 'Density (per km²)',
                'Growth Rate', 'World Population Percentage', '2022', '2020', '2015', '2010', '2000', '1990',
                '1980', '1970']]



# Prepare the data for the choropleth map
wp_df_years = wp_df[['ISO-3', 'Country'] + [str(year) for year in [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]]]
wp_df_melted = wp_df_years.melt(id_vars=["ISO-3", "Country"], var_name="Year", value_name="Population")

# Create the choropleth map
fig = px.choropleth(wp_df_melted, locations='ISO-3', color='Population', locationmode="ISO-3", scope="world",
                    width=1200, height=600, title='World Population by Country (1970-2070)',
                    hover_name="Country", hover_data={'ISO-3': False,}, projection='equirectangular',
                    range_color=(0, 200000000), animation_frame='Year', color_continuous_scale=px.colors.sequential.Viridis)

# Display the choropleth map
fig.show()