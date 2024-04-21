import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st


df = pd.read_csv('cause_of_deaths.csv')

# Sidebar navigation
st.sidebar.title("Navigation")
nav_option = st.sidebar.radio("Select View", ["World Map", "Scatter Plot", "Pie Chart", "Linear Plot"])
_, toggle_pop = st.columns([2,1])
divide_by_pop = False
toggled_once = False
diseases = ["Meningitis","Alzheimer's Disease and Other Dementias", "Parkinson's Disease","Nutritional Deficiencies","Malaria","Drowning","Interpersonal Violence",
            "Maternal Disorders","HIV/AIDS","Drug Use Disorders","Tuberculosis","Cardiovascular Diseases","Lower Respiratory Infections","Neonatal Disorders",	
            "Alcohol Use Disorders","Self-harm","Exposure to Forces of Nature","Diarrheal Diseases","Environmental Heat and Cold Exposure","Neoplasms",
            "Conflict and Terrorism","Diabetes Mellitus","Chronic Kidney Disease","Poisonings","Protein-Energy Malnutrition","Road Injuries","Chronic Respiratory Diseases",
            "Cirrhosis and Other Chronic Liver Diseases","Digestive Diseases","Fire, Heat, and Hot Substances","Acute Hepatitis","Total Deaths","Infectous deaths",
            "Communicable deaths","Unnatural deaths","Preventable Deaths", "Genetic caused Deaths"]

with toggle_pop:
    divide_by_pop = st.toggle('Deaths by 1000 people')
    if(divide_by_pop):
        for col in diseases:
            divisor_col = 'Population'
            toggled_once = True
            divisor = df[divisor_col]
            df[col] = df[col].div(divisor)*1000
    elif toggled_once:
        for col in diseases:
            divisor_col = 'Population'
            df[col] = df[col]*df[divisor_col]/1000

if nav_option == "World Map":
    
    # disease_to_show = "Malaria"
    from world_map import create_world_map
    
    world_map_fig = create_world_map(df, diseases)
    
    st.plotly_chart(world_map_fig, use_container_width=False, width=1000, height=800)

elif nav_option == "Scatter Plot":
    # Import the scatter plot code from scatter.py
    from scatter import create_scatter_plot

    st.title('Communicable vs Non-Communicable Deaths')
    scatter_plot = create_scatter_plot(divide_by_pop, df, diseases)
    st.plotly_chart(scatter_plot)

elif nav_option == "Linear Plot":
    from linear import create_line_plot
    
    st.title('Trend Analysis')
    selected_countries = st.multiselect('Select Countries/Territories', sorted(df['Country/Territory'].unique()))
    selected_cause_of_death = st.selectbox('Select Cause of Death', sorted(df.columns[6:]))
    line_plot = create_line_plot(selected_countries, selected_cause_of_death)
    st.plotly_chart(line_plot)  

elif nav_option == "Pie Chart":
    from pie_chart import create_pie_chart

    pie_chart = create_pie_chart(diseases)
    st.plotly_chart(pie_chart)   