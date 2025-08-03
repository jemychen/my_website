import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# In Streamlit, you can pass ANYTHING to write. It will automatically use some defaults from streamlit to plot it on the screen.
st.write("")

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")

    # In Streamlit, you can pass ANYTHING to write. It will automatically use some defaults from streamlit to plot it on the screen.
    st.write("df.head()")

    st.subheader('Data Summary')
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y_axis column", columns)
