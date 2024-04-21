import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st


df = pd.read_csv('cause_of_deaths.csv')

# Sidebar navigation
st.sidebar.title("Navigation")
nav_option = st.sidebar.radio("Select View", ["World Map", "Scatter Plot", "Linear Plot"])
_, toggle_pop = st.columns([2,1])
divide_by_pop = False
toggled_once = False
diseases = ["Meningitis","Alzheimer's Disease and Other Dementias", "Parkinson's Disease","Nutritional Deficiencies","Malaria","Drowning","Interpersonal Violence",
            "Maternal Disorders","HIV/AIDS","Drug Use Disorders","Tuberculosis","Cardiovascular Diseases","Lower Respiratory Infections","Neonatal Disorders",	
            "Alcohol Use Disorders","Self-harm","Exposure to Forces of Nature","Diarrheal Diseases","Environmental Heat and Cold Exposure","Neoplasms",
            "Conflict and Terrorism","Diabetes Mellitus","Chronic Kidney Disease","Poisonings","Protein-Energy Malnutrition","Road Injuries","Chronic Respiratory Diseases",
            "Cirrhosis and Other Chronic Liver Diseases","Digestive Diseases","Fire, Heat, and Hot Substances","Acute Hepatitis","Total Deaths","total infectous deaths",
            "total communicable deaths","Deaths due to unnatural causes", "Preventable Deaths",	"Deaths due to genetics"]

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
    
    
    showdis, showgdp, showdoc, showlifeexp = st.columns(4)
    disease_to_show = st.selectbox('Select Cause of Death', sorted(df.columns[6:]))
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
            df[variable_to_show] = df[disease_to_show]*(df["gdp per capita"])
            # if(divide_by_pop):
            #     df[variable_to_show] = df[variable_to_show] * 1000 / df["Population"]
    with showdoc:
        if st.button("Diseases/Doctors", key="diseases_w_doc"):
            variable_to_show = disease_to_show + "/doctors"
            df[variable_to_show] = df[disease_to_show]*(df["Physicains per 1000"])
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
        title_text='Life Expectancy',
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
    st.plotly_chart(fig, use_container_width=False, width=1000, height=800)

elif nav_option == "Scatter Plot":
    # Import the scatter plot code from scatter.py
    from scatter import create_scatter_plot

    st.title('Communicable vs Non-Communicable Deaths')
    years = df['Year'].unique()
    selected_year = st.slider('Select Year', min_value=min(years), max_value=max(years), value=min(years))
    scatter_plot = create_scatter_plot(selected_year, divide_by_pop, df, diseases)
    st.plotly_chart(scatter_plot)

elif nav_option == "Linear Plot":
    from linear import create_line_plot

    st.title('Trend Analysis')
    selected_country = st.selectbox('Select Country/Territory', sorted(df['Country/Territory'].unique()))
    selected_cause_of_death = st.selectbox('Select Cause of Death', sorted(diseases))
    line_plot = create_line_plot(selected_country, selected_cause_of_death, df)
    st.plotly_chart(line_plot)   