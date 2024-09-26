import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Title of the web app
st.title("My Streamlit App")

st.header("Welcome", divider='red')

# Main content
st.write("This application displays weather data.")

st.subheader("Metrics", divider='red')

col1, col2, col3, = st.columns(3)
st.metric(label="Temperature", value="75 °F", delta="4.2 °F")
st.metric(label="Wind", value="3mph", delta="-2%")
st.metric(label="Humidity", value="50%",delta="-30%")

st.subheader("Graph", divider='red')

# Create a simple DataFrame
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100)
})

# Display a line chart
st.line_chart(data.set_index('x'))
