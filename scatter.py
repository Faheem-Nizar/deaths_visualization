import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('cause_of_deaths.csv')

# Function to create the scatter plot
def create_scatter_plot(year, divide_by_pop, df):
    # Filter the data for the selected year
    year_data = df[df['Year'] == year]

    x_axis, y_axis = st.columns(2)

    # headings = sorted(df.columns[6:])
    with x_axis:
        option1 = st.selectbox('Variable in X-axis', df.columns[6:])

    # Add another dropdown menu to the second column
    with y_axis:
        option2 = st.selectbox('Variable in Y-axis', df.columns[6:])

    # Calculate communicable and non-communicable deaths per 1000 population
    year_data['communicable_per_1000'] = (year_data['total communicable deaths'] / year_data['Population']) * 1000
    year_data['non_communicable_per_1000'] = (year_data['Total Deaths'] - year_data['total communicable deaths']) / year_data['Population'] * 1000

    # Create the scatter plot
    fig = px.scatter(year_data, x='communicable_per_1000', y='non_communicable_per_1000', hover_name='Country/Territory',
                     hover_data=['communicable_per_1000', 'non_communicable_per_1000'],
                     title=f'Communicable vs Non-Communicable Deaths per 1000 Population ({year})')

    # Update the layout
    fig.update_layout(xaxis_title='Communicable Deaths per 1000',
                      yaxis_title='Non-Communicable Deaths per 1000')

    return fig

# Streamlit app
# st.title('Communicable vs Non-Communicable Deaths')

# Get the unique years from the data
# years = df['Year'].unique()

# Create a slider for the year
# selected_year = st.slider('Select Year', min_value=min(years), max_value=max(years), value=min(years))

# Create the scatter plot
# scatter_plot = create_scatter_plot(selected_year)

# Display the plot in Streamlit
# st.plotly_chart(scatter_plot)