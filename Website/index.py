import streamlit as st
import pandas as pd
from components.sidebar import sidebar
from components.modules import visuals
from components.modules import data

st.set_page_config(
    page_title="Traffic Fatalities", 
    page_icon="🌚", 
    layout="wide",
    initial_sidebar_state="expanded"
    )

#sidebar
sidebar()

#Title
st.title("🌚 Traffic Fatalities")

#Intro
st.header('Introduction')
st.write('This project investigates factors influencing traffic fatalities in Austin, Texas, from 2013 to 2019. Given Austin\'s rapid growth and increased congestion, identifying contributors to accidents is crucial for public safety. Insights gained will inform policymakers and law enforcement to enhance preventive measures and road safety infrastructure.')

#Data
data()

#Explore Analysis
visuals()

