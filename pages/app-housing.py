import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
st.title('California Housing Data(1990) by Xirun')
df = pd.read_csv('housing.csv')

house_price_filter = st.slider('Minimal Median House Price:', 0.0, 500001.0, 200000.0) 

# filter by house price
df = df[df.median_house_value >= house_price_filter]

# create a multi select
location_filter = st.sidebar.multiselect(
'Choose the location type',
df.ocean_proximity.unique(), # options
df.ocean_proximity.unique()) # defaults

df = df[df.ocean_proximity.isin(location_filter)]


income_level_filter = st.sidebar.radio(
    "Choose income level",
    ["Low","Medium","High"],
    index = None,
)
if income_level_filter == 'Low':
    df = df[df.median_income <= 2.5 ]
if income_level_filter == 'Medium':
    df = df[df.median_income > 2.5 & df.median_income <= 4.5]
if income_level_filter == 'High':
    df = df[df.median_income > 4.5 ]


# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)


# show dataframe
fig, ax = plt.subplots(figsize=(20, 15))
df.median_house_value.hist(bins=30)
st.pyplot(fig)
