import streamlit as st
import streamlit_shadcn_ui as ui

# Helper function to get item price
def get_price(item):
    prices = {
        "Red Toga": "$14.99",
        "Purple Toga": "$21.99",
        "White Toga": "$11.99"
    }
    
    # Handle case where item might not be found in the dictionary
    return prices.get(item, "Price Not Available")

# Initialize session state if not already initialized
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Define item images and prices
item_images = {
    "Red Toga": "redtoga.png",
    "Purple Toga": "purpletoga.png",
    "White Toga": "whitetoga.png"
}

# Create columns for layout
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])
r4col1, r4col2, r4col3 = st.columns([1, 2, 1])
r5col1, r5col2, r5col3 = st.columns([1, 2, 1])

options = []
options.extend(["Home", "Mihi Canistrum"])
selected_page = st.sidebar.radio("Navigation Menu", options=options)

# Home page logic
if selected_page == options[0]:
    with r1col2:  
        st.title("Home Page")
    
    with r2col2:
        taboptions = ["Mens", "Womans", "Childrens"]
        selected_home_tab = ui.tabs(taboptions)
        
        if selected_home_tab == taboptions[0]:
            with r3col2:
                st.title("Mens Clothing")
            
            # Display items and their buttons
            with r4col1:
                st.image(item_images["Red Toga"], caption="Red Toga. Price: $14.99")
            
            with r4col2:
                st.image(item_images["Purple Toga"], caption="Purple Toga. Price: $21.99", width=310)
            
            with r4col3:
                st.image(item_images["White Toga"], caption="White Toga. Price: $11.99", width=310)
            
            # Add to cart buttons
            with r5col1:
                if st.button("Add to cart", key="ATCRT1"):
                    st.session_state.cart.append("Red Toga")
                    
            with r5col2:
                if st.button("Add to cart", key="ATCPT1"):
                    st.session_state.cart.append("Purple Toga")
                    
            with r5col3:
                if st.button("Add to cart", key="ATCWT1"):
                    st.session_state.cart.append("White Toga")

# My Cart page logic
if selected_page == options[1]:
    with r1col2:
        st.title("My Cart")
        st.header("Items:")
        
        # Display each item from the cart
        for item in st.session_state.cart:
            if item in item_images:  # Ensure item exists in the dictionary
                price = get_price(item)  # Get the price
                st.image(item_images[item], caption=f"{item}. Price: {price}", width=200)
