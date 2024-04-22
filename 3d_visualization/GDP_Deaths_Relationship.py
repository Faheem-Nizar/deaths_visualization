import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Read the shapefile
world = gpd.read_file("updated_world.shp")

# Create a Folium map
m = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbpositron')

cmap = plt.cm.get_cmap('Reds')

# Add choropleth layer
folium.Choropleth(
    geo_data=world,
    data=world,
    columns=['ISO_A3', 'GDP_PER_CA'],  # Change column names accordingly
    key_on='feature.properties.ISO_A3',
    fill_color='YlGn',
    fill_opacity=0.8,
    line_opacity=0.3,
    legend_name='GDP PER CAPITA',
    highlight=True
).add_to(m)



for index, row in world.iterrows():
    # Get the coordinates of the country
    lat, lon = row.geometry.centroid.y, row.geometry.centroid.x

    # Get the value from the different column
    marker_value = round(row['death per'],2)
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
m.save('map.html')
