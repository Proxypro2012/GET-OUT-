import streamlit as st

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
options = []






options.extend(["Home", "My Cart"])
selected_page = st.sidebar.radio("Navigation Menu",options=options)

with r1col2:  
  if selected_page == options[0]:
    st.title("Home Page")

with r1col2:
  if selected_page == options[1]:
    st.title("My Cart")


