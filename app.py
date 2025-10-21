import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Streamlit SPA", layout="wide")

# Title of the page
st.title("Welcome to the Simple Streamlit SPA!")

# Sidebar for Navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

# Content based on selected page
if page == "Home":
    st.subheader("This is the Home Page")
    st.write("Here you can have an interactive dashboard or any widgets.")
    
    # Example interactive widgets
    st.write("Interact with the widgets below:")
    number = st.slider("Choose a number", 0, 100, 25)
    st.write(f"You chose: {number}")
    
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}!")

elif page == "About":
    st.subheader("About Us")
    st.write("""
        This is a simple Streamlit app example. 
        You can create Single Page Applications (SPA) 
        using Streamlit easily.
    """)

elif page == "Contact":
    st.subheader("Contact Us")
    st.write("You can contact us at contact@example.com")

