import streamlit as st
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from streamlit_folium import st_folium

# Read the shapefile

def plot_2_var_world_map(world):
    # Create a Folium map
    
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbpositron')

    cmap = plt.cm.get_cmap('Reds')

    #min_gdp = world['GDP_PER_CA'].min()
    #max_gdp = world['GDP_PER_CA'].max()
    #selected_min_gdp, selected_max_gdp = st.slider("Select GDP per capita range to display the desired countries", min_gdp, max_gdp, (min_gdp, max_gdp))

    #filtered_world = world[(world['GDP_PER_CA'] >= selected_min_gdp) & (world['GDP_PER_CA'] <= selected_max_gdp)]

    columns = ['GDP_PER_CA', 'Population', 'LifeExpect', 'Physicains']  # Add your desired columns here

    selected_column = st.selectbox("Select desired parameter:", columns)

    # Get min and max values for selected column
    min_value = world[selected_column].min()
    max_value = world[selected_column].max()

    # Slider to select value range
    selected_min_value, selected_max_value = st.slider(f"Select range for {selected_column}:", min_value, max_value, (min_value, max_value))

    # Filter the dataframe based on selected column and value range
    filtered_world = world[(world[selected_column] >= selected_min_value) & (world[selected_column] <= selected_max_value)]


    # Add choropleth layer
    folium.Choropleth(
        geo_data=filtered_world,
        data=filtered_world,
        columns=['ISO_A3', 'GDP_PER_CA'],  # Change column names accordingly
        key_on='feature.properties.ISO_A3',
        fill_color='YlGn',
        fill_opacity=0.8,
        line_opacity=0.3,
        legend_name='GDP PER CAPITA',
        highlight=True
    ).add_to(m)

    # Add markers for death rates
    for index, row in filtered_world.iterrows():
        # Get the coordinates of the country
        lat, lon = row.geometry.centroid.y, row.geometry.centroid.x

        # Get the value from the different column
        marker_value = round(row['death per'], 2)
        country = row['Country/Te'] 

        marker_color = mcolors.rgb2hex(cmap(marker_value/10))

        # Create a marker with a popup showing the value
        folium.CircleMarker(
            location=[lat, lon],
            radius=marker_value,  # Adjust the divisor to control the size of the marker
            color=marker_color,  # Marker color
            fill=True,
            fill_color=marker_color,  # Marker fill color
            fill_opacity=0.7,
            popup=folium.Popup(f"<div style='font-size: 16px;'>Country: <b>{country}</b> <br> Death per 1000: <b>{marker_value}</b></div>", max_width=300)  # Popup text with increased font size
        ).add_to(m)

    # Display the map
    st_folium(m,width="100%")
