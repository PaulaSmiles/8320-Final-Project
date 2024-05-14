
 
import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="Percent change for Pueblo, CO",
    page_icon="✅",
    layout="wide",
)

# Write the title and introductory text
st.write("""
# Percent Change for Pueblo, CO
This app visualizes percentage changes for different categories and codes.
""")

# Load the CSV data
csv_file = "percentage_change.csv"
percentage_change_data = pd.read_csv(csv_file)

# Check the structure of the data
st.write("Data Overview:", percentage_change_data.head())

# Ensure the data types are correct
percentage_change_data['Percentage Change'] = pd.to_numeric(percentage_change_data['Percentage Change'], errors='coerce')

# Pivot the data to format it for the chart
pivot_data = percentage_change_data.pivot_table(
    index=percentage_change_data.index,
    columns=['Category', 'Code'],
    values='Percentage Change'
)

# Display the pivoted data
st.write("Pivoted Data Overview:", pivot_data.head())

# Display the chart
st.line_chart(pivot_data)

# Top-level filters
job_filter = st.selectbox("Select the Category", pd.unique(percentage_change_data["Category"]))
