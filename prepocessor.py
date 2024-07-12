import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


def preprocess():
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC')
    df = df.drop_duplicates()
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)
    return df
