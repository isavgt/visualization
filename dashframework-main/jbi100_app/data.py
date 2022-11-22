import pandas as pd
import plotly.express as px

def get_data():
    # Read data
    df = px.data.iris()
    df_airbnb = pd.read_csv('Airbnb_Open_Data.csv')
    # Any further data preprocessing can go her

    return df

get_data()