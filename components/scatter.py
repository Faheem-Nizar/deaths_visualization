import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
# df = pd.read_csv('cause_of_deaths.csv')

# Function to create the scatter plot
def create_scatter_plot( divide_by_pop, df, diseases):
    # Filter the data for the selected year
    year_data = df


    _, toggle_cat = st.columns([2,1])
    toggle_status = False
    
    category = ["Infectous deaths","Communicable deaths","Unnatural deaths","Preventable Deaths", "Genetic caused Deaths"]

    with toggle_cat:
        toggle_status = st.toggle('Category-wise')

    if toggle_status == False:
        x_axis, y_axis = st.columns(2)

        # headings = sorted(df.columns[6:])
        with x_axis:
            x_axis_var = st.selectbox('Variable in X-axis', diseases)

        # Add another dropdown menu to the second column
        with y_axis:
            y_axis_var = st.selectbox('Variable in Y-axis', diseases)
    
    else:
        _, dropdown_for_cat = st.columns([2, 1])

        # headings = sorted(df.columns[6:])
        with dropdown_for_cat:
            x_axis_var = st.selectbox('Category to Show', category)
            y_axis_var = "non " + x_axis_var
            if(x_axis_var == "Unnatural deaths"):
                y_axis_var = "Natural Deaths"
            
            year_data[y_axis_var] = year_data["Total Deaths"] - year_data[x_axis_var]
        # Add another dropdown menu to the second column
        
    years = df['Year'].unique()
    selected_year = st.slider('Select Year', min_value=min(years), max_value=max(years), value=min(years))
    year_data = df[df['Year'] == selected_year]
    # Calculate communicable and non-communicable deaths per 1000 population
    # year_data['communicable_per_1000'] = (year_data['total communicable deaths'] / year_data['Population']) * 1000
    # year_data['non_communicable_per_1000'] = (year_data['Total Deaths'] - year_data['total communicable deaths']) / year_data['Population'] * 1000
    text = ""
    d_text = ""
    if(toggle_status):
        d_text = ""
    else:
        d_text = "Deaths "
    if(divide_by_pop):
        text = "per 1000"
    else:
        text = ""
    # Create the scatter plot
    fig = px.scatter(year_data, x=x_axis_var, y=y_axis_var, hover_name='Country/Territory',
                     hover_data=[x_axis_var, y_axis_var], size="Population", size_max=50,
                     color="Continent", 
                     title=f'{x_axis_var} vs {y_axis_var} {d_text}{text}({selected_year})')

    # Update the layout
    fig.update_layout(xaxis_title=f'{x_axis_var} {d_text}{text}',
                      yaxis_title=f'{y_axis_var} {d_text}{text}', width=700, height=700)

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