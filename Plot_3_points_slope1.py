# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 22:16:39 2024

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

# Select the slope columns
slope_columns = ['06/07/21', '02/05/22']

# Check if the slope columns exist
for column in slope_columns:
    if column not in gdf.columns:
        raise ValueError(f"The column '{column}' is not in the GeoDataFrame.")

# Create a DataFrame with the selected slopes
plot_df = selected_points[['Number'] + slope_columns].copy()
plot_df.rename(columns={'Number': 'Point Number'}, inplace=True)

# Melt the DataFrame to prepare for plotting
plot_df = plot_df.melt(id_vars='Point Number', 
                       value_vars=slope_columns,
                       var_name='Measurement', value_name='Slope')

# Plot using Plotly
fig = px.scatter(plot_df, x='Point Number', y='Slope', color='Measurement',
                 title='Slopes of Selected Points', labels={'Point Number': 'Point Number', 'Slope': 'Slope'})

# Modify the X axis range
fig.update_xaxes(tickvals=selected_point_numbers, ticktext=selected_point_numbers, dtick=1)

# Save the plot as an image file
image_file_path = r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Plots\Sampled_points\slope_comparison_plot.png'
fig.write_image(image_file_path)

fig.show()

image_file_path
