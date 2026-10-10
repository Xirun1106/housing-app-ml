import streamlit as st

st.set_page_config(page_title="Housing App ML", page_icon="🏠", layout="centered")

st.title("🏠 Housing App ML")
st.subheader("California Housing Data Explorer")

st.markdown("""
Welcome to the Housing App ML project! 

This application helps you explore and analyze California housing data from 1990. 
You can filter properties by price, location type, and income level to discover insights 
about the housing market.

### Features:
- 📊 Interactive price filtering
- 🗺️ Geographic visualization
- 📈 Distribution analysis
- 🎯 Multi-criteria filtering

### Get Started:
Click the button below to explore the housing data, or use the sidebar navigation to access the app.
""")

st.markdown("---")

# Button to navigate to app-housing page
if st.button("🚀 Go to Housing Data Explorer", use_container_width=True, key="nav_button"):
    st.switch_page("pages/app-housing.py")

st.markdown("---")
st.markdown("""
**Data Source:** California Housing Dataset (1990)

Created by Xirun | ML Housing Data Explorer
""")
