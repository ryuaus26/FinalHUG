import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px

# Load data
wp_df = pd.read_csv('world_population.csv')
wp_df.columns = ['Rank', 'ISO-3', 'Country', 'Capital', 'Continent', '2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']
wp_df = wp_df[['Rank', 'ISO-3', 'Country', 'Capital', 'Continent', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage', '2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']]

# Prepare the data for the choropleth map
wp_df_years = wp_df[['ISO-3', 'Country'] + [str(year) for year in [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]]]
wp_df_melted = wp_df_years.melt(id_vars=["ISO-3", "Country"], var_name="Year", value_name="Population")

# Calculate the best fit line for each country
country_fits = wp_df_melted.groupby('Country').apply(lambda x: np.polyfit(x['Year'].astype(int), x['Population'], 1))
slopes = pd.Series([x[0] for x in country_fits], index=country_fits.index)
intercepts = pd.Series([x[1] for x in country_fits], index=country_fits.index)

# Add future years and corresponding population values
future_years = [year for year in range(2030, 3000, 5)]
future_data = []
for idx, row in wp_df_melted[wp_df_melted['Year'] == '2022'].iterrows():
    iso3 = row["ISO-3"]
    country = row['Country']
    slope = slopes[country]
    intercept = intercepts[country]
    for year in future_years:
        future_population = slope * year + intercept
        future_data.append({'ISO-3': iso3, 'Country': country, 'Year': year, 'Population': future_population})

wp_df_melted = pd.concat([wp_df_melted, pd.DataFrame(future_data)], ignore_index=True)

# Create the choropleth map
fig = px.choropleth(wp_df_melted, locations='ISO-3',
                    color='Population', locationmode="ISO-3", scope="world", width=1200, height=600,
                    title='World Population by Country (1970-2110)', hover_name="Country",
                    hover_data={'ISO-3': False,}, projection='equirectangular', range_color=(0, 1000000000),
                    animation_frame='Year', color_continuous_scale=px.colors.sequential.Viridis,
                    )

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
    
fig.update_geos(
    resolution = 50
)

# Display the choropleth map
fig.show()