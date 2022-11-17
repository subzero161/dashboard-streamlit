####Import packages
import streamlit as st
import pandas as pd
import numpy as np

STAFF_COLUMN = 'date/time'
DATA_URL = 'https://healthdata.gov/resource/nqtp-eetp.csv'


def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data   

df = load_data()
#df = df.reset_index()
df

##check pandas pivot function