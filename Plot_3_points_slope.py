# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:10:14 2024

@author: Huzaifa
"""

import geopandas as gpd
import plotly.express as px

# Define the file path
gpkg_file = r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Plots\Sampled_points\Slope.gpkg'

# Read the .gpkg file
gdf = gpd.read_file(gpkg_file)

# Define the point numbers you want to select
selected_point_numbers = [8, 9, 11]  # Replace with the desired point numbers

# Select the specified points based on the "Number" column
selected_points = gdf[gdf['Number'].isin(selected_point_numbers)]

# Select the elevation columns
elevation_columns = ['06/07/21', '02/05/22']

# Check if the elevation columns exist
for column in elevation_columns:
    if column not in gdf.columns:
        raise ValueError(f"The column '{column}' is not in the GeoDataFrame.")

# Create a DataFrame with the selected elevations
plot_df = selected_points[['Number'] + elevation_columns].copy()
plot_df.rename(columns={'Number': 'Point Number'}, inplace=True)

# Melt the DataFrame to prepare for plotting
plot_df = plot_df.melt(id_vars='Point Number', 
                       value_vars=elevation_columns,
                       var_name='Measurement', value_name='Elevation')

# Plot using Plotly
fig = px.scatter(plot_df, x='Point Number', y='Elevation', color='Elevation',
                 title='Slope Variation between Points of 2 Selected Surveys', labels={'Point Number': 'Point Number', 'Elevation': 'Elevation'})

# Modify the X axis range
fig.update_xaxes(tickvals=selected_point_numbers, ticktext=selected_point_numbers, dtick=1)

# Save the plot as an image file
image_file_path = r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Plots\Sampled_points\elevation_comparison_plot5.png'
fig.write_image(image_file_path)

fig.show()

image_file_path