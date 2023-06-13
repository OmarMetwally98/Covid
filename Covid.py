####################################################### LIBRARIES ########################################################
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit import components
#########################################################################################################################

df = pd.read_csv('Covid.csv')

st.set_page_config(page_title = 'Covid Dashboard',
                    page_icon = 'bar_chart:',
                    layout = 'wide'
)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar for filtering options
st.sidebar.title('Filter Data')

# Create sidebar select boxes
country = st.sidebar.selectbox('Select Country', df['Country/Region'].unique())
region = st.sidebar.selectbox('Select WHO Region', df['WHO Region'].unique())

# Apply filters
filtered_data = df
if country:
    filtered_data = df[df['Country/Region'] == country]
if region:
    filtered_data = df[df['WHO Region'] == region]

    st.title("Covid Cases Worldwide")

    fig = px.choropleth(
    data_frame=filtered_data,
    locations='Country/Region',  # Column containing the country names
    locationmode='country names',
    color='Confirmed',  # Column to determine the color of the regions
    hover_name='Country/Region',  # Column to display on hover
    color_continuous_scale='Viridis',  # Choose a color scale
    projection='natural earth'  # Choose a map projection
)



# Set customdata for hover details
    fig.data[0].customdata = filtered_data[['Confirmed', 'Deaths', 'Recovered']]


    fig.update_layout(
    width=1000,  # Set the width of the figure in pixels
    height=600  # Set the height of the figure in pixels
)

    st.plotly_chart(fig)

# Filter and sort the data to get the top 10 countries with the highest number of malaria cases
top_10_countries = filtered_data.sort_values("Confirmed", ascending=False).head(10)
top_10_countries = top_10_countries[::-1]  

st.title("Top 10 Countries with the Highest Number of Covid Cases ")

# Create the bar chart using Plotly
fig = px.bar(top_10_countries, x='Country/Region', y='Confirmed')

# Customize the layout
fig.update_layout(
    xaxis_title='Country/Region',
    yaxis_title='Confirmed Cases',
    title='Top 10 Countries with Confirmed Cases'
)

# Display the chart using Streamlit
st.plotly_chart(fig)

# Filter and sort the data to get the top 10 countries with the highest number of malaria cases
top_10_countries_d = filtered_data.sort_values("Deaths", ascending=False).head(10)
top_10_countries_d = top_10_countries_d[::-1]  

st.title("Top 10 Countries with the Highest Number of Deaths Cases ")

# Create the bar chart using Plotly
fig = px.bar(top_10_countries, x='Country/Region', y='Deaths')

# Customize the layout
fig.update_layout(
    xaxis_title='Country/Region',
    yaxis_title='Deaths Cases',
    title='Top 10 Countries with Confirmed Cases'
)

# Display the chart using Streamlit
st.plotly_chart(fig)


st.title("Top Region with Deaths Cases ")

# Group the data by organization and calculate the total deaths
organization_deaths = filtered_data.groupby('WHO Region')['Deaths'].sum().reset_index()

