import streamlit as st
import pandas as pd

def visuals():
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
    v2c1.table(v2df)

    vis3.write('Hypothesis 3: During daylight hours, there are significantly less traffic fatalities than during nighttime hours.')
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
    v3data = {'R-squared value': ['0.04563 (low correlation, <0.2)'], 'Adjusted R-squared': [0.0023429], 'Standard Error': [ 0.2556736]}
    v3df = pd.DataFrame(v3data)
    v3c1.table(v3df)

    vis4.write('Hypothesis 4: When the driver is suspected to be impaired, more traffic fatalities occur.')
    v4c1, v4c2 = vis4.columns(2)
    v4c1.image('components/images/visual4.png')
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
    v5c1.image('components/images/visual5.png')
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
    v6c1.image('components/images/visual6.png')
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
