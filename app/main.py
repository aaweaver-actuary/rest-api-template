import streamlit as st
from .utils import ENDPOINT, get_price

st.title("Simple Pricing Model API")

# Side-by-side input boxes for base rate and mod factor:
col1, col2 = st.columns(2)
with col1:
    base_rate = st.number_input("Base Rate", min_value=0.0, format="%.2f", value=100.0)
with col2:
    mod_factor = st.number_input("Mod Factor", min_value=0.9, max_value=2.0, format="%.2f", value=1.0)

if st.button("Calculate the rate!", type='primary'):
    try:
        # rate = asyncio.run(get_price(base_rate, mod_factor, ENDPOINT))
        rate = get_price(base_rate, mod_factor, ENDPOINT)
        st.write(rate)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Not yet calculated :(")

st.markdown(f"[See API Docs ->]({ENDPOINT.replace('/calculate', '/docs')})")