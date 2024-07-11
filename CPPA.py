import streamlit as st
import pickle

import numpy as np
import pandas as pd

rforest = pickle.load(open('Random_forest.pkl','rb'))
Ada_boost = pickle.load(open('Ada_boost.pkl','rb'))

st.title('Car-Price Prediction App')

st.header('Fill out the below mentioned Details to know the price of the Car')

Options = st.sidebar.selectbox('Machine Learning Model',['Random Forest','AdaBoost'])

Brand_Name = st.selectbox('Maker',['Maruti','Hyundai','Mahindra','Tata','Others','Ford','Honda','Toyota',
                                      'Chevrolet','Renault','Volkswagen'])
Year = st.slider('Year',1992,2020)
Km_driven = st.slider('KMs driven',1,2000000)
Fuel = st.selectbox('Fuel',['Diesel','Petrol','CNG','LPG','Electric'])
Seller = st.selectbox('Seller',['Individual','Dealer','Trustmark Dealer'])
Transmission = st.selectbox('Transmission',['Manual','Automatic'])
Ownership = st.selectbox('Ownership',['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])


if st.button('Predict'):
    
    if Brand_Name == "Maruti":
          Brand_Name = 5
    elif Brand_Name =='Hyundai':
          Brand_Name = 3
    elif Brand_Name =='Mahindra':
          Brand_Name = 4
    elif Brand_Name =='Others':
          Brand_Name = 6
    elif Brand_Name =='Ford':
          Brand_Name = 1
    elif Brand_Name =='Honda':
          Brand_Name = 2                          
    elif Brand_Name =='Toyota':
          Brand_Name = 9
    elif Brand_Name =='Chevrolet':
          Brand_Name = 0
    elif Brand_Name =='Renault':
          Brand_Name = 7              
    else:
          Brand_Name = 10

    if Fuel == 'Diesel':
          Fuel = 1          
    elif Fuel == 'Petrol':
          Fuel = 4
    elif Fuel == 'CNG':
          Fuel = 0           
    elif Fuel == 'LPG':
          Fuel = 3
    else:
          Fuel = 2

    if Seller == 'Individual':
          Seller = 1
    elif Seller == 'Dealer':
          Seller = 0     
    else:
          Seller = 2  

    if Ownership == 'First Owner':
          Ownership = 0
    elif Ownership == 'Second Owner':
          Ownership = 2
    elif Ownership == 'Third Owner':
          Ownership = 4
    elif Ownership == 'Fourth and Above Owner':
          Ownership = 1 
    else:
          Ownership = 3

    if Transmission == 'Manual':
          Transmission = 1
    else:
          Transmission = 0

    test = np.array([Brand_Name,Year,Km_driven,Fuel,Seller,Transmission,Ownership])
    test = test.reshape(1,7)
    if Options == 'Random Forest':
           st.success(rforest.predict(test)[0])
    else:
          st.success(Ada_boost.predict(test)[0])      

