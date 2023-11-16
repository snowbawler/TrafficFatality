import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(
            "## About\n"
            "This project combines data from NASA and"
            " the city of Austin to determine relationships"
            " between moon phases, the day of the week, and"
            " traffic fatalities.💬\n"
        )
        st.markdown("---")
        st.markdown("# Goals")
        st.markdown(
            "📖 The goal of this project is to determine" 
            " relationships between the moon phases, days"
            " of the week and traffic fatalities in Austin"
            ", Texas."
        )
        st.markdown(
            "Austin's rapid growth has heightened traffic"
            " congestion, increasing road risks. Identifying"
            " causes of accidents is vital for policymakers and "
            " law enforcement to enhance safety measures and infrastructure."
        )
        st.markdown("Made by [snowbawler](https://github.com/snowbawler)")
        st.markdown("---")
