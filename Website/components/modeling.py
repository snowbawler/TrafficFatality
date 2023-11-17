import streamlit as st
import pandas as pd

import numpy as np
import matplotlib.pylab as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def modelingCode():
    df = pd.read_csv('https://raw.githubusercontent.com/snowbawler/TrafficFatality/main/project_data.csv')

    #dropping unnecessary features
    df = df.drop(['Fatal.Crash.Number', 'Unnamed: 0', 'Case.Number', 'Location', 'DateTime', 'Date'], axis=1)

    #encoding categorical variables
    label_encoder = LabelEncoder()
    df['Type'] = label_encoder.fit_transform(df['Type'])
    df['Month'] = label_encoder.fit_transform(df['Month'])
    df['Day'] = label_encoder.fit_transform(df['Day'])
    df['Killed.driver.pass'] = label_encoder.fit_transform(df['Killed.driver.pass'])
    df['Speeding'] = label_encoder.fit_transform(df['Speeding'])
    df['Ran.Red.Light.or.Stop.Sign'] = label_encoder.fit_transform(df['Ran.Red.Light.or.Stop.Sign'])
    df['DL.Status.incident'] = label_encoder.fit_transform(df['DL.Status.incident'])
    df['Suspected.Impairment'] = label_encoder.fit_transform(df['Suspected.Impairment'])
    df['Type.of.road'] = label_encoder.fit_transform(df['Type.of.road'])
    df['MoonPhaseCat'] = label_encoder.fit_transform(df['MoonPhaseCat'])
    
    # Define the target variable and features
    target_variable = 'MoonPhaseCat'
    features = ['Type', 'Number.of.Fatalities', 'Month', 'Day', 'Hour',
        'Killed.driver.pass', 'Ran.Red.Light.or.Stop.Sign',
        'DL.Status.incident', 'Suspected.Impairment', 'Type.of.road',
        'Speeding']
    
    # Split the data into training and testing sets
    X = df[features]
    y = df[target_variable]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate the Random Forest model
    rf_model = RandomForestClassifier(max_depth=6)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)
    
    # Get feature importances from the model
    feature_importances = rf_model.feature_importances_

    # Create a DataFrame to store feature importances along with feature names
    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})

    # Sort the DataFrame by importance values in descending order
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    # Create a bar plot to visualize feature importances
    fig = plt
    fig.figure(figsize=(10, 6))
    fig.bar(importance_df['Feature'], importance_df['Importance'])
    fig.xlabel('Features')
    fig.ylabel('Importance')
    fig.title('Random Forest Feature Importance Classifying Moon Phases')
    fig.xticks(rotation=45, ha='right')
    fig.tight_layout()

    return f"Random Forest Accuracy: {rf_accuracy:.4f}", fig

def modelingCode2():
    df = pd.read_csv('https://raw.githubusercontent.com/snowbawler/TrafficFatality/main/project_data.csv')

    #dropping unnecessary features
    df = df.drop(['Fatal.Crash.Number', 'Unnamed: 0', 'Case.Number', 'Location', 'DateTime', 'Date'], axis=1)

    #encoding categorical variables
    label_encoder = LabelEncoder()
    df['Type'] = label_encoder.fit_transform(df['Type'])
    df['Month'] = label_encoder.fit_transform(df['Month'])
    df['Day'] = label_encoder.fit_transform(df['Day'])
    df['Killed.driver.pass'] = label_encoder.fit_transform(df['Killed.driver.pass'])
    df['Speeding'] = label_encoder.fit_transform(df['Speeding'])
    df['Ran.Red.Light.or.Stop.Sign'] = label_encoder.fit_transform(df['Ran.Red.Light.or.Stop.Sign'])
    df['DL.Status.incident'] = label_encoder.fit_transform(df['DL.Status.incident'])
    df['Suspected.Impairment'] = label_encoder.fit_transform(df['Suspected.Impairment'])
    df['Type.of.road'] = label_encoder.fit_transform(df['Type.of.road'])
    df['MoonPhaseCat'] = label_encoder.fit_transform(df['MoonPhaseCat'])
    
    # Define the target variable and features
    target_variable = 'Speeding'
    features = ['Type', 'Number.of.Fatalities', 'Month', 'Day', 'Hour',
        'Killed.driver.pass', 'Ran.Red.Light.or.Stop.Sign',
        'DL.Status.incident', 'Suspected.Impairment', 'Type.of.road',
        'MoonPhaseCat']
    
    # Split the data into training and testing sets
    X = df[features]
    y = df[target_variable]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate the Random Forest model
    rf_model = RandomForestClassifier(max_depth=6)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)
    
    # Get feature importances from the model
    feature_importances = rf_model.feature_importances_

    # Create a DataFrame to store feature importances along with feature names
    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})

    # Sort the DataFrame by importance values in descending order
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    # Create a bar plot to visualize feature importances
    fig = plt
    fig.figure(figsize=(10, 6))
    fig.bar(importance_df['Feature'], importance_df['Importance'])
    fig.xlabel('Features')
    fig.ylabel('Importance')
    fig.title('Random Forest Feature Importance Predicting Speeding')
    fig.xticks(rotation=45, ha='right')
    fig.tight_layout()

    return f"Random Forest Accuracy: {rf_accuracy:.4f}", fig
