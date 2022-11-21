import streamlit as st
import pandas as pd

st.title("Datenfilter")
st.markdown("Beschreibung")


#DF Load Cache 
def load_data():
  path = ""
  return pd.read_excel("path_to_file.xls", sheet_name="Sheet1")
df = load_data()

#DF Filter
df = df[["StartTime"]]

#Sidebar für Filter
st.sidebar.header('Filter')
st.sidebar.slider
