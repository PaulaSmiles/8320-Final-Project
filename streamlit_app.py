
 
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
# My first app
Hello *world!*
""")

# Load the CSV data
csv_file = "percentage_change.csv"
percentage_change_data = pd.read_csv(csv_file)

# Display the chart
st.line_chart(percentage_change_data)

# top-level filters
job_filter = st.selectbox("Select the Category", pd.unique(df["Category"]))
