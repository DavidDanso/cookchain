import streamlit as st
import langchain_helper

st.title("🥙 CookChain: AI Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American", "Ghanaian"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.markdown(response['formatted_text'])

