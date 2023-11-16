import streamlit as st
import pandas as pd
from components.sidebar import sidebar

st.set_page_config(
    page_title="Traffic Fatalities", 
    page_icon="🌚", 
    layout="wide",
    initial_sidebar_state="expanded"
    )

sidebar()

st.title("🌚 Traffic Fatalities") #Title

#Intro
st.header('Introduction')
st.write('This project investigates factors influencing traffic fatalities in Austin, Texas, from 2013 to 2019. Given Austin\'s rapid growth and increased congestion, identifying contributors to accidents is crucial for public safety. Insights gained will inform policymakers and law enforcement to enhance preventive measures and road safety infrastructure.')

#Data
st.header('Data')
col1, col2 = st.columns(2)
col1.write('Traffic fatality data from the years 2013 through 2019 was sourced from [data.austintexas.gov](https://data.austintexas.gov/Public-Safety/2019-APD-Traffic-Fatality-Data/egpd-hqdi/explore/query/SELECT%0A%20%20%60type%60%2C%0A%20%20%60fatal_crash_number%60%2C%0A%20%20%60number_of_fatalities%60%2C%0A%20%20%60case_number%60%2C%0A%20%20%60location%60%2C%0A%20%20%60area%60%2C%0A%20%20%60date%60%2C%0A%20%20%60month%60%2C%0A%20%20%60day%60%2C%0A%20%20%60hour%60%2C%0A%20%20%60time%60%2C%0A%20%20%60related%60%2C%0A%20%20%60killed_driver_pass%60%2C%0A%20%20%60speeding%60%2C%0A%20%20%60ran_red_light_or_stop_sign%60%2C%0A%20%20%60dl_status_incident%60%2C%0A%20%20%60suspected_impairment%60%2C%0A%20%20%60restraint_type%60%2C%0A%20%20%60type_of_road%60%2C%0A%20%20%60failure_to_stop_and_render%60%2C%0A%20%20%60x_coord%60%2C%0A%20%20%60y_coord%60%2C%0A%20%20%60homeless%60/page/filter). Features of these data sets include:')
col1.write(['Type of fatality', 'Number of fatalities', 'Case number', 'Location', 'Date', 'Day of the week', 'Time', 'Whether the driver or passenger was killed', 'Speeding', 'If the driver ran a red light or stop sign', 'Driver\'s license status', 'Suspected impairment', 'Type of road'])
col2.write('Moon phase data was sourced from [nasa.gov](https://svs.gsfc.nasa.gov/4442). Features of this data includes:')
col2.write(['Month', 'Day', 'Time', 'Moon phase', 'Moon age', 'Moon diameter', 'Moon distance from Earth', 'Moon phase category'])
st.write('Steps taken to clean data:')
st.markdown("""
- Clean Moon Data: Load each moon_phase dataset of each year independently as text files. Text files then are read into a table separating columns by tab delimiters and rows by enter delimiters. Label each column. Each annual dataset is mutated alongside the corresponding year and merged together with dplyr row bound functions. Group in order by date and time.
- Clean Traffic Fatality Data: Load in traffic_fatality dataset as csv. Remove extraneous columns: “related”, “restraint type”,  “x and y coord”, “fail to stop and render aid”, and “Homeless”. Group in order by date and time.
- Merge Datasets: Merge by common date and time. Ignore and remove unmerged/missing value rows. Remove extraneous “date” and “time” columns. Convert date columns to date format.
""")
df = pd.read_csv('https://raw.githubusercontent.com/snowbawler/TrafficFatality/main/project_data.csv')
st.write(df.head().drop('Unnamed: 0', axis=1))

#Explore Analysis
st.header('Exploratory Analysis')
vis1, vis2, vis3, vis4, vis5, vis6 = st.tabs(['Visualization 1', '2', '3', '4', '5', '6'])

vis1.write('Hypothesis 1: During a waxing gibbous, there are more occurrences of traffic fatalities in Austin, Texas.')
v1c1, v1c2 = vis1.columns(2)
v1c1.image('components/images/visual1.png')
v1c2.code(
    'ggplot(project, aes(x = MoonPhaseCat)) +\n'
        'geom_bar(fill = "mediumslateblue") +\n'
        'labs(title = "Number of Fatalities by Moon Phase Category",\n'
        '   x = "Moon Phase Category", \n'
        '   y = "Count of Fatalities") +\n'
        'theme(axis.text.x = element_text(angle = 45, hjust = 1))'
)

vis2.write('Hypothesis 2: High use roadways have significantly more traffic fatalities than any other roadways.')
v2c1, v2c2 = vis2.columns(2)
v2c1.image('components/images/visual2.png')
v2c2.code(
    'project %>%\n'
    '   group_by(Type.of.road) %>%\n'
    '   summarise(FatalitiesCount = n()) %>%\n'
    '   ggplot(aes(x = reorder(Type.of.road, FatalitiesCount),\n' 
    '       y = FatalitiesCount)) +\n'
    '   geom_bar(fill = "aquamarine3", stat = "identity") +\n'
    '   labs(title = "Number of Fatalities by Road Type",\n' 
    '       x = "Road Type",\n'
    '       y = "Count of Fatalities") +\n'
    '   theme(axis.text.x = element_text(angle = 45, hjust = 1))'
)
v2data = {'R-squared value': ['0.0231 (low correlation, <0.2)'], 'Adjusted R-squared': [-0.005264], 'Standard Error': [0.2566465]}
v2df = pd.DataFrame(v2data)
vis2.table(v2df)

vis3.write('Hypothesis 2: High use roadways have significantly more traffic fatalities than any other roadways.')
v3c1, v3c2 = vis3.columns(2)
v3c1.image('components/images/visual3.png')
v3c2.code(
    'project %>%\n'
    '   group_by(Type.of.road) %>%\n'
    '   summarise(FatalitiesCount = n()) %>%\n'
    '   ggplot(aes(x = reorder(Type.of.road, FatalitiesCount),\n' 
    '       y = FatalitiesCount)) +\n'
    '   geom_bar(fill = "aquamarine3", stat = "identity") +\n'
    '   labs(title = "Number of Fatalities by Road Type",\n' 
    '       x = "Road Type",\n'
    '       y = "Count of Fatalities") +\n'
    '   theme(axis.text.x = element_text(angle = 45, hjust = 1))'
)
v3data = {'R-squared value': ['0.0231 (low correlation, <0.2)'], 'Adjusted R-squared': [-0.005264], 'Standard Error': [0.2566465]}
v3df = pd.DataFrame(v3data)
vis3.table(v3df)

vis4.write('Hypothesis 2: High use roadways have significantly more traffic fatalities than any other roadways.')
v4c1, v4c2 = vis4.columns(2)
v4c1.image('components/images/visual4.png')
v4c2.code(
    'project %>%\n'
    '   group_by(Type.of.road) %>%\n'
    '   summarise(FatalitiesCount = n()) %>%\n'
    '   ggplot(aes(x = reorder(Type.of.road, FatalitiesCount),\n' 
    '       y = FatalitiesCount)) +\n'
    '   geom_bar(fill = "aquamarine3", stat = "identity") +\n'
    '   labs(title = "Number of Fatalities by Road Type",\n' 
    '       x = "Road Type",\n'
    '       y = "Count of Fatalities") +\n'
    '   theme(axis.text.x = element_text(angle = 45, hjust = 1))'
)

v4data = {'R-squared value': ['0.0231 (low correlation, <0.2)'], 'Adjusted R-squared': [-0.005264], 'Standard Error': [0.2566465]}
v4df = pd.DataFrame(v4data)
vis4.table(v4df)

vis5.write('Hypothesis 2: High use roadways have significantly more traffic fatalities than any other roadways.')
v5c1, v5c2 = vis5.columns(2)
v5c1.image('components/images/visual5.png')
v5c2.code(
    'project %>%\n'
    '   group_by(Type.of.road) %>%\n'
    '   summarise(FatalitiesCount = n()) %>%\n'
    '   ggplot(aes(x = reorder(Type.of.road, FatalitiesCount),\n' 
    '       y = FatalitiesCount)) +\n'
    '   geom_bar(fill = "aquamarine3", stat = "identity") +\n'
    '   labs(title = "Number of Fatalities by Road Type",\n' 
    '       x = "Road Type",\n'
    '       y = "Count of Fatalities") +\n'
    '   theme(axis.text.x = element_text(angle = 45, hjust = 1))'
)
v5data = {'R-squared value': ['0.0231 (low correlation, <0.2)'], 'Adjusted R-squared': [-0.005264], 'Standard Error': [0.2566465]}
v5df = pd.DataFrame(v5data)
vis5.table(v3df)


