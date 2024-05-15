import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px

wp_df = pd.read_csv('world_population.csv')


wp_df.columns = ['Rank','ISO-3','Country','Capital','Continent','2022','2020','2015',
                 '2010','2000','1990','1980','1970','Area (km²)','Density (per km²)','Growth Rate',
                 'World Population Percentage']

wp_df = wp_df[['Rank','ISO-3','Country','Capital','Continent', 'Area (km²)','Density (per km²)',
              'Growth Rate', 'World Population Percentage','2022','2020','2015','2010','2000','1990',
              '1980','1970']]


wp_df_years = wp_df[['ISO-3','Country','1970','1980','1990','2000','2010','2015','2020','2022']]


wp_df_melted = wp_df_years.melt(id_vars=["ISO-3", "Country"], var_name="Year", value_name="Population")


fig = px.choropleth(wp_df_melted, locations = 'ISO-3', color = 'Population', 
                    locationmode="ISO-3", scope="world", width = 1200, height = 600,
                    title = 'World Population by Country (1970-2022)', 
                    hover_name="Country",
                    hover_data = {'ISO-3':False,},
                    projection = 'orthographic',
                    range_color=(0, 600000000), #to fix the scale
                    animation_frame='Year', #added new column as the animation frame
                    color_continuous_scale=px.colors.sequential.Viridis)
 
fig.show()