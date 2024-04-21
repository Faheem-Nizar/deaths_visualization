import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('cause_of_deaths.csv')

# Function to create the line plot
def create_line_plot(country, cause_of_death, df):
    # Filter the data for the selected country and cause of death
    filtered_data = df[(df['Country/Territory'] == country) & (df[cause_of_death].notnull())]

    # Create the line plot
    fig = px.line(filtered_data, x='Year', y=cause_of_death,
                  title=f'Deaths per Year: {cause_of_death} in {country}')

    # Update the layout
    fig.update_layout(xaxis_title='Year',
                      yaxis_title='Deaths')

    return fig

# Streamlit app
# st.title('Communicable vs Non-Communicable Deaths')

# Get the unique years from the data
# years = df['Year'].unique()

# Create a slider for the year
# selected_year = st.slider('Select Year', min_value=min(years), max_value=max(years), value=min(years))

# Create the line plot
# line_plot = create_line_plot(selected_year)

# Display the plot in Streamlit
# st.plotly_chart(line_plot)
