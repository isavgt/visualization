import pandas as pd
import numpy as np
import plotly.express as px

def read_data():
    # Read data
    df = pd.read_csv('Airbnb_Open_Data.csv', low_memory=False)
    
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
        df.loc[x, 'price']=int(df.loc[x, 'price'].replace('$', '').replace(' ','').replace(',',''))

    #change faulty values into the right one
    df.loc[df['neighbourhood group']=="brookln",'neighbourhood group']="Brooklyn"
    df.loc[df['neighbourhood group']=="manhatan",'neighbourhood group']="Manhattan"

    #interpolate missing values for the neighbourhood by searching similar values
    for x in range(len(df)):
        if pd.isnull(df.loc[x,'neighbourhood group']):
            for y in range(len(df)):
                if df.loc[x,'neighbourhood']== df.loc[y,'neighbourhood']:
                    df.loc[x,'neighbourhood group']= df.loc[y,'neighbourhood group']

    df.to_csv('cleaned_airbnb_data.csv', index = False)
    return df


read_data()




