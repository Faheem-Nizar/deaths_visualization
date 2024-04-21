import streamlit as st
import pandas as pd
import plotly.express as px

def create_pie_chart(diseases):
    df = pd.read_csv('output_aggregated_data.csv')
    st.title("Disease Deaths per Continent")
    selected_disease = st.selectbox("Select Disease:", diseases)
    selected_year = st.slider("Select Year:", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].max())

    # Filter the data for the selected disease and year
    disease_data = df[(df['Year'] == selected_year) & (df[selected_disease] > 0)]

    # Calculate the total deaths per continent for the selected disease
    continent_deaths = disease_data.groupby('Continent')[selected_disease].sum().reset_index()

    # Create the pie chart using Plotly Express
    fig = px.pie(continent_deaths, values=selected_disease, names='Continent',
                title=f'Percentage of {selected_disease} Deaths per Continent in {selected_year}')
    return fig