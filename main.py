import streamlit as st
import streamlit_shadcn_ui as ui

if 'cart' not in st.session_state:
    st.session_state.cart = []


r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])

options = []






options.extend(["Home", "My Cart"])
selected_page = st.sidebar.radio("Navigation Menu",options=options)


if selected_page == options[0]:
 with r1col2:  
     st.title("Home Page")
 with r2col2:
     taboptions = ["Mens", "Womans", "Childrens"]
     selected_home_tab = ui.tabs(taboptions)
     if selected_home_tab == taboptions[0]:
      with r3col2:
          st.title("Mens Clothing")
    

if selected_page == options[1]:
   with r1col2: 
    st.title("My Cart")


