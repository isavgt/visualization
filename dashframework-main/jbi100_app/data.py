import pandas as pd
import numpy as np
import plotly.express as px

def read_data():
    # Read data
    df = pd.read_csv('Airbnb_Open_Data.csv')
    
    #drop rows with NaN values (only the columns which are essential to our goal)
    df.dropna(subset = ['lat','long','NAME','price'], inplace=True)

    #drop duplicates
    df.drop_duplicates(subset= ['id'], keep='first') 

    #availability can only be between 0 and 365 days
    df.drop(df[df['availability 365'] > 365].index, inplace=True) 
    df.drop(df[df['availability 365'] < 0].index, inplace=True)

    #review scores can only be between 1 and 5
    df.drop(df[df['review rate number'] > 5].index, inplace=True) 
    df.drop(df[df['review rate number'] < 1].index, inplace=True)

    #reset indexes of dataframe
    df = df.reset_index()

    #turn values of column price into integers to be able to work with them
    for x in range(len(df)):
        df['price'][x]=int(df['price'][x].replace('$', '').replace(' ','').replace(',',''))

    #change faulty values into the right one
    df[df['neighbourhood group']=="brookln"]="Brooklyn"
    df[df['neighbourhood group']=="manhatan"]="Manhattan"

    #interpolate missing values for the neighbourhood by searching similar values
    for x in range(len(df)):
        if pd.isnull(df['neighbourhood group'][x]):
            for y in range(len(df)):
                if df['neighbourhood'][x] == df['neighbourhood'][y]:
                    df['neighbourhood group'][x] = df['neighbourhood group'][y]

    df.to_csv('dashframework-main\cleaned_airbnb_data_test.csv', index = False)
    return df


read_data()




