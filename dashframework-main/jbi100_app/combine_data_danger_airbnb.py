## IMPORTANT: It takes approximately 10 hours to run this file on a standard laptop. This file creates 'airbnb_with_crimes_cleaned.csv'.
## It calculates the log of the sum of all crimes multiplied with their weights
import pandas as pd
import numpy as np

#load danger database with score
df = pd.read_csv(r'DatabaseWithScore.csv')
# df.drop('Unnamed: 0', inplace = True, axis = 1)
df_crime = df.copy()

#load cleaned_airbnb_data
df_airbnb = pd.read_csv(r'cleaned_airbnb_data.csv')
df_airbnb.drop('level_0', inplace = True, axis = 1)
df_airbnb

#is going to add the crime data to the Airbnb database
from math import sqrt
radius = 0.0027027 #500 meter

danger_score_int = 0
nr_felonies_int = 0
nr_misdemeanors_int = 0
nr_violations_int = 0
danger_score_list = []
nr_felonies_list = []
nr_misdemeanors_list = []
nr_violations_list = []

#iterates over the airbnb database
# i is de index 
for i in range(len(df_airbnb)):
    airbnb_lat = df_airbnb['latitude'][i]
    airbnb_long = df_airbnb['longitude'][i]
    #iterates over the crime database. So for every airbnb it goes over all the crimes
    for a in range(len(df_crime)):
        crime_lat = df_crime['Latitude'][a]
        crime_long = df_crime['Longitude'][a]
        pyt = sqrt((abs(airbnb_lat - crime_lat) ** 2) + (abs(airbnb_long - crime_long) ** 2))
        #looks if the crime is within 500 meter of the Airbnb
        if pyt <= radius:
            danger_score_int += df_crime['SCORE'][a]
            if df_crime['LAW_CAT_CD'][a] == 'F':
                nr_felonies_int += 1
            elif df_crime['LAW_CAT_CD'][a] == 'M':
                nr_misdemeanors_int += 1
            elif df_crime['LAW_CAT_CD'][a] == 'V':
                nr_violations_int += 1
                
    #total danger score per Airbnb
    danger_score_list.append(danger_score_int)
    #total number of felonies per Airbnb
    nr_felonies_list.append(nr_felonies_int)
    #total number of misdemeanors per Airbnb
    nr_misdemeanors_list.append(nr_misdemeanors_int)
    #total number of violations per Airbnb
    nr_violations_list.append(nr_violations_int)
    danger_score_int = 0
    nr_violations_int = 0 
    nr_misdemeanors_int = 0
    nr_felonies_int = 0 
    
df_airbnb['nr_of_felonies'] = nr_felonies_list
df_airbnb['nr_of_misdemeanors'] = nr_misdemeanors_list
df_airbnb['nr_of_violations'] = nr_violations_list
df_airbnb['danger_score'] = danger_score_list



df = pd.read_csv('airbnb_with_crimes.csv')
df['Danger Score']= np.log(df['danger_score']).round(decimals = 1)

df.index = range(len(df))

df = df.drop('index', axis = 1)
df = df.drop('Unnamed: 0.1', axis =1)
df = df.drop('index_2', axis =1)
df = df.drop('level_0', axis =1)
df = df.reset_index(level=0)

df_airbnb.to_csv('airbnb_with_crimes_cleaned.csv')