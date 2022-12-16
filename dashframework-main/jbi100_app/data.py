import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import ast

#load dataset and generalize column names
df = pd.read_csv(r'C:\Users\20203171\OneDrive - TU Eindhoven\2022-2023\Q2\Visualization\Project\listings.csv.gz')
df.columns=[col.lower().replace(" ","_") for col in df.columns]

#dropping columns that are mostly missing values
df.drop(columns=["license",'calendar_updated','bathrooms','neighbourhood'], axis=1, inplace=True)

#dropping unnecessary columns
df.drop(columns=['source','listing_url', 'scrape_id', 'last_scraped','picture_url', 'host_id',
        'host_url','host_about','host_verifications','host_location','host_neighbourhood', 'host_response_time', 
        'host_response_rate', 'host_acceptance_rate', 'host_thumbnail_url', 'host_picture_url','host_has_profile_pic', 
        'host_identity_verified','minimum_minimum_nights','maximum_minimum_nights', 'minimum_maximum_nights',
        'maximum_maximum_nights', 'minimum_nights_avg_ntm','maximum_nights_avg_ntm','calendar_last_scraped','instant_bookable',
        'calculated_host_listings_count','calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms',
       'calculated_host_listings_count_shared_rooms','host_listings_count','host_total_listings_count', 'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review',
       'last_review',  'review_scores_accuracy','review_scores_cleanliness', 'review_scores_checkin',
        'review_scores_communication', 'review_scores_location','review_scores_rating', 'reviews_per_month', 'minimum_nights',
        'maximum_nights','description', 'neighborhood_overview','host_since', 'has_availability', 'availability_30', 
        'availability_60','availability_90', 'availability_365','beds'],axis=1,inplace=True)

#renaming columns
df = df.rename(columns={'neighbourhood_cleansed': 'neighbourhood', 'neighbourhood_group_cleansed': 'neighbourhood_group'})

#drop missing values for several columns
df.dropna(subset = ['latitude','longitude','name','price','bathrooms_text'], inplace=True)

#drop duplicates
df.drop_duplicates(subset= ['id'], keep='first') 

#resetting index of df
df = df.reset_index()

#removing dollar signs, commas and blankspaces from columns price and service_fee
for x in range(len(df)):
    df['price'][x]=float(df['price'][x].replace('$', '').replace(' ','').replace(',',''))
    df['amenities'][x] = ast.literal_eval(df['amenities'][x])
    if df['host_is_superhost'][x] == 'f':
        df['host_is_superhost'][x] = False
    else:
        df['host_is_superhost'][x] = True
    
    
df['Private/Shared'] = 0
df['nr_bathrooms'] = 0

for x in range(len(df)):
    shared = 'shared'
    Shared = 'Shared'
    if shared in df['bathrooms_text'][x] or Shared in df['bathrooms_text'][x] :
        df['Private/Shared'][x] = 'Shared'
    else:
        df['Private/Shared'][x] = 'Private'
        
    df['nr_bathrooms'][x] = df['bathrooms_text'][x].split(" ")[0]
    #correcting errors manually 
    if df['nr_bathrooms'][x] == 'Shared' or df['nr_bathrooms'][x] == 'Private' or df['nr_bathrooms'][x] == 'Half-bath':
        df['nr_bathrooms'][x] = '0.5'
        
    df['nr_bathrooms'][x] = float(df['nr_bathrooms'][x])
    
df.drop(columns=['bathrooms_text'],axis=1,inplace=True)

