import pandas as pd

# df = pd.read_csv('C:/Users/20213338/Documents/uni/jaar 2/Q2/Visualization/NYPD_Arrest_Data__Year_to_Date_.csv')


def read_dangerous_data():
    # Read data
    df = pd.read_csv('NYPD_Arrest_Data__Year_to_Date_.csv')

    # drop rows with NaN values (only the columns which are essential to our goal)
    df.dropna(subset=['Latitude', 'Longitude', 'PD_DESC', 'LAW_CAT_CD', 'OFNS_DESC'], inplace=True)

    # drop rows where PD_DESC is equal to null, because we cannot classify if something is dangerous or not if it does not have a discribtion
    df.drop(df[df['PD_DESC'] == '(null)'].index, inplace=True)

    # drops rows with invalid Law_Cat_cd
    df.drop(df[df['LAW_CAT_CD'] == 'I'].index, inplace=True)

    # drops the race of the misdemeanants
    df.drop('PERP_RACE', inplace=True, axis=1)

    # reset indexes of dataframe
    df = df.reset_index()

    dangerous = ['RAPE', 'SEX CRIMES', 'JOSTLING', 'ARSON', 'DANGEROUS WEAPONS',
                 'ASSAULT 3 & RELATED OFFENSES', 'FELONY ASSAULT',
                 'PETIT LARCENY', 'GRAND LARCENY', 'OFF. AGNST PUB ORD SENSBLTY &', 'ROBBERY',
                 'OTHER OFFENSES RELATED TO THEF',
                 'BURGLARY', 'MURDER & NON-NEGL. MANSLAUGHTE', 'GRAND LARCENY OF MOTOR VEHICLE',
                 'DISORDERLY CONDUCT', 'OFFENSES AGAINST THE PERSON',
                 'HARRASSMENT 2', 'HOMICIDE-NEGLIGENT,UNCLASSIFIE',
                 'OFFENSES AGAINST PUBLIC SAFETY', 'HOMICIDE-NEGLIGENT-VEHICLE', 'KIDNAPPING & RELATED OFFENSES',
                 'FRAUDULENT ACCOSTING', 'UNLAWFUL POSS. WEAP. ON SCHOOL', 'KIDNAPPING']

    for index in range(len(df['OFNS_DESC'])):
        value = df['OFNS_DESC'][index]  # strinng
        if value not in dangerous:
            df.drop(index, inplace=True, axis=0)

    return df


read_dangerous_data()