def main():
    import streamlit as st
    import pandas as pd
    from components.sidebar import sidebar
    from components.modules import visuals, data, modeling, modeling2, ethics
    from components.modeling import modelingCode, modelingCode2



    import numpy as np
    import matplotlib.pylab as plt
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder

    st.set_option('deprecation.showPyplotGlobalUse', False)

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

    #Model
    modeling()
    modelrun = st.button("Run Model Code")
    result = ''
    fig = ''
    if modelrun:
        result, fig = modelingCode()
        st.code(result)
        plot1 = st.pyplot(fig)
        
    modeling2()

    result2 = ''
    fig2 = ''
    modelrun2 = st.button("Run Model Code for Speeding")
    if modelrun2:
        result2, fig2 = modelingCode2()
        st.code(result2)
        plot2 = st.pyplot(fig2)

    #Ethics
    ethics()

