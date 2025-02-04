import streamlit as st
import streamlit_shadcn_ui as ui

if 'cart' not in st.session_state:
    st.session_state.cart = []


r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])
r4col1, r4col2, r4col3 = st.columns([1, 2, 2])
r5col1, r5col2, r5col3 = st.columns([1, 2, 1])

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
      with r4col1:
          st.image("redtoga.png", caption="Red Toga. Price: $14.99")
      with r4col2:
          st.image("purpletoga.png", caption="Purple Toga. Price: $21.99", width=310)
      with r4col3:
          st.image("whitetoga.png", caption="White Toga. Price: $11.99", width=310)
    
    

if selected_page == options[1]:
   with r1col2: 
    st.title("My Cart")


