import streamlit as st
import plotly.express as px

# Title for the Streamlit app
st.title("INSEE Data Visualization")

# User inputs for metric and year range
metric = st.selectbox("Select Metric", ["Unemployment", "Poverty", "GDP"])
year_range = st.slider("Select Year Range", 2000, 2023, (2010, 2020))

# When the user clicks the "Generate Graph" button
if st.button("Generate Graph"):
    # Generate a sample graph (replace with actual logic for INSEE data)
    fig = px.line(x=range(year_range[0], year_range[1] + 1), y=[5, 6, 7, 8])
    st.plotly_chart(fig)
