import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_world_map(df, diseases):
    showdis, showgdp, showdoc, showlifeexp = st.columns(4)
    disease_to_show = st.selectbox('Select Cause of Death', sorted(diseases))
    variable_to_show = disease_to_show
    df[variable_to_show] = df[disease_to_show]
    # if(divide_by_pop):
    #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]

    with showdis:
        if st.button("Diseases", key="diseases"):
            variable_to_show = disease_to_show
            df[variable_to_show] = df[disease_to_show]
            # if(divide_by_pop):
            #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]
    with showgdp:
        if st.button("Diseases/GDP", key="diseases_w_gdp"):
            variable_to_show = disease_to_show + "/gdp"
            df[variable_to_show] = df[disease_to_show]/(df["gdp per capita"])
            # if(divide_by_pop):
            #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]
    with showdoc:
        if st.button("Diseases/Doctors", key="diseases_w_doc"):
            variable_to_show = disease_to_show + "/doctors"
            df[variable_to_show] = df[disease_to_show]/(df["Physicains per 1000"])
            # if(divide_by_pop):
            #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]
    with showlifeexp:
        if st.button("Diseases/Life exp.", key="diseases_w_lifeexp"):
            variable_to_show = disease_to_show + "/life_expectancy"
            df[variable_to_show] = df[disease_to_show]*1000000/(df["Life expectancy"])
            # if(divide_by_pop):
            #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]
    
    

    
    fig = px.choropleth(
        data_frame=df,
        locations='Code',
        color=variable_to_show,
        animation_frame='Year',
        color_continuous_scale='viridis',
        hover_name='Country/Territory',
    )
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=25),
        width=900,
        height=600,
        geo=dict(
            scope='world',
            projection=go.layout.geo.Projection(type='equirectangular'),
            showlakes=True,
            lakecolor='rgba(0,0,0,0)',
            bgcolor= 'rgba(0,0,0,0)'
        ),
    )
    
    return fig