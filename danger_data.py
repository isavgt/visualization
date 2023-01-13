import pandas as pd
import numpy as np

df = pd.read_csv('airbnb_with_crimes.csv')
df['Danger Score']= np.log(df['danger_score']).round(decimals = 1)
df.to_csv('airbnb_with_crimes.csv', index = False)
