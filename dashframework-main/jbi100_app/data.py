import pandas as pd
import plotly.express as px

def get_data():
    # Read data
    df = px.data.iris()
    df_airbnb = pd.read_csv('Airbnb_Open_Data.csv')
    print(df_airbnb.columns)
    # Any further data preprocessing can go here

    return df

get_data()

