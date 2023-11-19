import streamlit as st

# Import your main Streamlit app
from your_app import main  # Replace with your actual Streamlit app filename

st.set_page_config(layout="wide")

# Run the Streamlit app and render to HTML
with st.script_request_queue():
    main()
