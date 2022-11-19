####Import packages
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
header = st.container()
dataset =st.container() 
features = st.container()
model_training = st.container()


with header:
    st.title('Welcome to streamlit assignment')
    st.text('Unfortunate data posted by HHS about layoffs')



#DATA_URL = 'https://healthdata.gov/resource/nqtp-eetp.csv'

with dataset:
    st.header('FY 2023 HHS Contingency Staffing Plan for a Lapse in Appropriation')
    st.text('HHS’ contingency plans for agency operations in the absence of appropriations ')

    hhs_data = pd.read_csv('https://healthdata.gov/resource/nqtp-eetp.csv')
    #hhs_data = hhs_data[['staff_involved','cdc','cms',]]
    #st.dataframe(data = hhs_data, x="staff_involved", y="cdc","cms","fda")
    st.bar_chart(data = hhs_data, x="staff_involved", y=("cdc","cms","fda"))
    st.table(hhs_data)
    #st.subheader('Pickup Location ID distribution')
    #pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts().head(50))
    #st.bar_chart(pulocation_dist)

#def load_data():
    #data = pd.read_csv(DATA_URL)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    #return data   

#df = load_data()
#df = df.reset_index()
#df

##check pandas pivot function