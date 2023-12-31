import streamlit as st
import pandas as pd


def data():
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


def visuals():
    st.header('Exploratory Analysis')
    vis1, vis2, vis3, vis4, vis5, vis6 = st.tabs(['Visualization: 1', '2', '3', '4', '5', '6'])

    vis1.write('Hypothesis 1: During a waxing gibbous, there are more occurrences of traffic fatalities in Austin, Texas.')
    v1c1, v1c2 = vis1.columns(2)
    v1c1.image('Website/components/images/visual1.png')
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
    v2c1.image('Website/components/images/visual2.png')
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
    v2c1.table(v2df)

    vis3.write('Hypothesis 3: During daylight hours, there are significantly less traffic fatalities than during nighttime hours.')
    v3c1, v3c2 = vis3.columns(2)
    v3c1.image('Website/components/images/visual3.png')
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
    v3data = {'R-squared value': ['0.04563 (low correlation, <0.2)'], 'Adjusted R-squared': [0.0023429], 'Standard Error': [ 0.2556736]}
    v3df = pd.DataFrame(v3data)
    v3c1.table(v3df)

    vis4.write('Hypothesis 4: When the driver is suspected to be impaired, more traffic fatalities occur.')
    v4c1, v4c2 = vis4.columns(2)
    v4c1.image('Website/components/images/visual4.png')
    v4c2.code(
        'project$Suspected.Impairment <- fct_reorder(project$Suspected.Impairment,\n'
        'project$Number.of.Fatalities,\n' 
        '.fun = sum, .desc = TRUE\n'
        ')\n'
        'ggplot(project, aes(x = Suspected.Impairment)) +\n'
        '    geom_bar(fill = "plum4",\n'
        '        color = "black", \n'
        '        size = 0.7, \n'
        '        alpha = 0.8\n'
        '    ) +\n'
        '    labs(title = "Number of Fatalities by Suspected Impairment", \n'
        '         x = "Suspected Impairment", \n'
        '         y = "Count of Fatalities"\n'
        '         ) +\n'
        '    theme_minimal() +\n'
        '    theme(\n'
        '        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1),\n'
        '        panel.grid.major = element_blank(),\n'
        '        panel.grid.minor = element_blank(),\n'
        '        panel.background = element_rect(fill = "white"),\n'
        '        axis.line = element_line(color = "black"),\n'
        '        legend.position = "none"\n'
        '    )\n'
        ')'
    )

    v4data = {'R-squared value': ['0.077680 (low correlation)'], 'Adjusted R-squared': [0.0357566], 'Standard Error': [0.251584]}
    v4df = pd.DataFrame(v4data)
    v4c1.table(v4df)

    vis5.write('Hypothesis 5: Proportionally, more traffic fatalities occur during the weekend than during weekdays in Austin, Texas.')
    v5c1, v5c2 = vis5.columns(2)
    v5c1.image('Website/components/images/visual5.png')
    v5c2.code(
        'project$Number.of.Fatalities <- as.numeric(project$Number.of.Fatalities)\n'
        'project <- project %>%\n'
        '    mutate(Weekday = ifelse(Day %in% c("sat", "sun"), "Weekend", "Weekday"))\n'
        '# Aggregate the data to get the count of fatalities for each weekday/weekend\n'
        'agg_data <- project %>%\n'
        '    group_by(Weekday) %>%\n'
        '    summarise(Fatalities = sum(Number.of.Fatalities))\n'
        '# Create a bar plot\n'
        'ggplot(agg_data, aes(x = Weekday, y = Fatalities, fill = Weekday)) +\n'
        '    geom_bar(stat = "identity", position = "dodge", color = "black") +\n'
        '    labs(title = "Number of Fatalities by Weekday/Weekend", \n'
        '         x = "Day of Week", \n'
        '         y = "Count of Fatalities") +\n'
        '    scale_fill_manual(values = c("Weekday" = "seagreen3", "Weekend" = "purple1")) +\n'
        '    theme_minimal()'
    )
    v5data = {'R-squared value': ['0.009688 (very low correlation), <0.2)'], 'Adjusted R-squared': [-0.0035657], 'Standard Error': [0.256429]}
    v5df = pd.DataFrame(v5data)
    v5c1.table(v3df)

    vis6.write('Hypothesis 6: Those with expired or suspended licenses are less likely to be involved in traffic fatalities.')
    v6c1, v6c2 = vis6.columns(2)
    v6c1.image('Website/components/images/visual6.png')
    v6c2.code(
        'ggplot(project, aes(x = DL.Status.incident, fill = DL.Status.incident)) +\n'
        '    geom_bar(stat = "count", position = "dodge", color = "black") +\n'
        '    labs(title = "Number of Fatalities by Driver\'s Licence Status",\n'
        '        x = "Driver\'s License Status",\n'
        '        y = "Count of Fatalities") +\n'
        '    theme_minimal() +\n'
        '    theme(axis.text.x = element_text(angle = 45, hjust = 1),\n'
        '        legend.position = "none")\n'
    )
    v6data = {'R-squared value': ['0.0677567 (low correlation)'], 'Adjusted R-squared': [0.007612065], 'Standard Error': [0.2554623]}
    v6df = pd.DataFrame(v6data)
    v6c1.table(v3df)

def modeling():
    st.header("Modeling")
    st.write('The task chosen was to predict whether or not a specific moon phase data affected driver behavior to cause traffic fatalities.')
    st.write('To complete this task, a classification model is required. A Random Forest model would suffice given tasks where a single Decision Tree may be too sensitive to the specifics of the training data. In this way, contrasts in feature strengths will show greater and give decipherable information.')
    st.write('Preprocessing the data required dropping class unrelated features such as concrete observations of the moon, “street names”, “extraneous date information”, and “case numbers”. It also involved mutating and grouping categorical values into numerical ones using a label encoder.')
    st.code(
        '#dropping unnecessary features\n'
        'df = df.drop([\'Fatal.Crash.Number\', \'Unnamed: 0\', \'Case.Number\', \'Location\', \'DateTime\', \'Date\'], axis=1)\n'
        '#encoding categorical variables\n'
        'from sklearn.preprocessing import LabelEncoder\n'
        'label_encoder = LabelEncoder()\n'
        'df[\'Type\'] = label_encoder.fit_transform(df[\'Type\'])\n'
        'df[\'Month\'] = label_encoder.fit_transform(df[\'Month\'])\n'
        'df[\'Day\'] = label_encoder.fit_transform(df[\'Day\'])\n'
        'df[\'Killed.driver.pass\'] = label_encoder.fit_transform(df[\'Killed.driver.pass\'])\n'
        'df[\'Speeding\'] = label_encoder.fit_transform(df[\'Speeding\'])\n'
        'df[\'Ran.Red.Light.or.Stop.Sign\'] = label_encoder.fit_transform(df[\'Ran.Red.Light.or.Stop.Sign\'])\n'
        'df[\'DL.Status.incident\'] = label_encoder.fit_transform(df[\'DL.Status.incident\'])\n'
        'df[\'Suspected.Impairment\'] = label_encoder.fit_transform(df[\'Suspected.Impairment\'])\n'
        'df[\'Type.of.road\'] = label_encoder.fit_transform(df[\'Type.of.road\'])\n'
        'df[\'MoonPhaseCat\'] = label_encoder.fit_transform(df[\'MoonPhaseCat\'])\n'
    )
    st.write('Then, assign “Moon Phase Category” as the target variable and all other columns as features; and use a random forest model to first split the data into 80% training data and 20% test data.')
    st.code(
        '''# Define the target variable and features
target_variable = 'MoonPhaseCat'
features = ['Type', 'Number.of.Fatalities', 'Month', 'Day', 'Hour',
    'Killed.driver.pass', 'Ran.Red.Light.or.Stop.Sign',
    'DL.Status.incident', 'Suspected.Impairment', 'Type.of.road',            
    'Phase', 'Age', 'Diam', 'Dist', 'RA', 'Dec', 'Slon',
    'Slat', 'Elon', 'Elat', 'AxisA']

# Split the data into training and testing sets
X = df[features]
y = df[target_variable]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)'''
    )
    st.write('Using the random forest model, we train and evaluate the accuracy of the model.')
    st.code(
        '''# Train and evaluate the Random Forest model
rf_model = RandomForestClassifier(max_depth=6)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")'''
    )
    
def modeling2():
    st.write('The accuracy of the model results is extremely low. The model has difficulty in modeling the feature data with the correct moon classification, showing very little correlation between the training data features and driver behavior.')
    st.write('Running a model with speeding as the target variable further explains the lack of correlation between traffic fatalities and moon phases. Analysis of features importance also gives insight to strong causal and outcome predictors of reckless behavior in traffic fatalities.')
    
def ethics():
    st.header("Ethics")
    st.markdown("""
        - Unintended Consequences - (Reflect on Product) 
            - The dip in traffic fatalities during first and last quarters does not reflect the overall dip in traffic fatalities, rather it reflects the data removed during preprocessing as a result of non-matching occurrences between corresponding moon phases and data-times recorded.
            - It's crucial to consider unintended consequences that may arise from our analysis of traffic fatalities and moon phases. One unintended consequence could be the misinterpretation of correlation as causation. One may misinterpret the findings as the moon has definite effects on traffic fatalities and that fatal traffic events are more likely to occur when the moon is in waxing gibbous, or less likely during first and last quarters. This oversimplification could lead to misconceptions and a dismissal of other relevant factors influencing traffic accidents.
        - People Affected - (Anticipate People)
            - The unintended consequences may cause changes in public perception and behavior. If media outlets or individuals sensationalize the findings, there is a risk that some Austin drivers alter their behavior based on the perceived influence of the moon. For example, drivers might become overly cautious during certain moon phases or overly confident during others, leading to changes in driving patterns that could impact road safety.
        - Continuous Improvement - (Act on Process)
            - To mitigate potential misconstruction, our data needs to clearly communicate the lack of a significant correlation between moon phases and traffic fatalities. Descriptions should provide context on the limitations of the analysis and the importance of considering multiple factors influencing road safety; acknowledge uncertainties and the need for further research to validate any observed patterns.
    """)
    
def discussion():
    pass

def conclusion():
    pass