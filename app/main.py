import streamlit as st
import requests

st.title("Simple Pricing Model API")

# Side-by-side input boxes for base rate and mod factor:
col1, col2 = st.columns(2)
with col1:
    base_rate = st.number_input("Base Rate", min_value=0.0, format="%.2f")
with col2:
    mod_factor = st.number_input("Mod Factor", min_value=0.0, format="%.2f")