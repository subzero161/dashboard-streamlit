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


def get_data(hhs_data):
    hhs_data = hhs_data = pd.read_csv('https://healthdata.gov/resource/nqtp-eetp.csv')
    return hhs_data
#DATA_URL = 'https://healthdata.gov/resource/nqtp-eetp.csv'

with dataset:
    st.header('FY 2023 HHS Contingency Staffing Plan for a Lapse in Appropriation')
    st.text('HHS’ contingency plans for agency operations in the absence of appropriations ')

    hhs_data = pd.read_csv('https://healthdata.gov/resource/nqtp-eetp.csv')
    hhs_data = hhs_data.rename(columns={'staff_involved':'Staff Involved','cdc':'Centers for Disease Control and Prevention','cms': 'Centers for Medicare and Medicaid Services', 'fda': 'Food and Drug Administration'})
    #hhs_data = hhs_data[['staff_involved','cdc','cms',]]
    #st.dataframe(data = hhs_data, x="staff_involved", y="cdc","cms","fda")
    st.bar_chart(data = hhs_data, x="Staff Involved", y=("Centers for Disease Control and Prevention","Centers for Medicare and Medicaid Services","Food and Drug Administration"))
    #st.table(hhs_data)
    st.subheader('CDC staff layoff')
    cdc = pd.DataFrame(hhs_data['Staff Involved'], hhs_data['Centers for Disease Control and Prevention'].head())
    st.bar_chart(cdc)

with model_training:
    st.header('Model is trained here')
    st.text('Chose the parameters that you wannna run')

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('what should be the max depth of the model', min_value=10, max_value=100, value=20, step=10)

    n_estimators = sel_col.selectbox('How many trees should there be', options=[100,200,300,'No limit'], index = 0)

    sel_col.text('Here is a list of features in my data')
    sel_col.write(hhs_data.columns)

    input_feature = sel_col.text_input('Which feature should be used as import feature', 'Centers for Disease Control and Prevention')
   
    if n_estimators == 'No limit':
        regr = RandomForestRegressor(max_depth=max_depth)
    else:
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    #regr = RandomForestRegressor(max_depth=max_depth, n_estimators=number_of_trees)
    X = hhs_data[[input_feature]]
    y = hhs_data[['Centers for Disease Control and Prevention']] 
    
    regr.fit(X, y)
    prediction = regr.predict(y)

    display_col.subheader('Mean absolute error:')
    display_col.write(mean_absolute_error(y, prediction))

    display_col.subheader('Mean absolute error:')
    display_col.write(mean_absolute_error(y, prediction)) 
    
    display_col.subheader('Mean square error:')
    display_col.write(mean_square_error(y, prediction)) 
    
    display_col.subheader('R squared error error:')
    display_col.write(r2_score(y, prediction)) 

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