import streamlit as st
import joblib
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load Random Forest model
model = joblib.load('/Users/goli/Documents/random_forest_modelCars.joblib')

with open('/Users/goli/Documents/brands.pkl', 'rb') as f:
    cars = pickle.load(f)

gear_encoder = OneHotEncoder()
gear_encoder.fit([['Manual'], ['Automatic']])

energy_encoder = OneHotEncoder()
energy_encoder.fit([['Gasoline'], ['Diesel'], ['Electric']])

brand_encoder = LabelEncoder()
brand_encoder.fit(cars)


# Create input fields
st.title('Car Price Prediction')
departement = st.text_input('Enter Departement:')
annee = st.number_input('Enter Year:', min_value=2017, max_value=2023, step=1)
kilometrage = st.number_input('Enter Kilometrage:', min_value=0, step=1000)
gear = st.selectbox('Select Gear:', options=['Manual', 'Automatic'])
energy = st.selectbox('Select Energy:', options=['Gasoline', 'Diesel', 'Electric'])
brand = st.text_input('Enter Brand:')
model_name = st.text_input('Enter Model:')

def preprocess_input(departement, annee, kilometrage, gear, energy, brand, model_name):
    Gear_encoded = gear_encoder.transform([[gear]]).toarray()[0]
    Energy_encoded = energy_encoder.transform([[energy]]).toarray()[0]
    Brand_encoded = brand_encoder.transform([brand])[0]
    return [departement, annee, kilometrage] + list(Gear_encoded) + list(Energy_encoded) + [Brand_encoded]


# Predict button
if st.button('Predict'):
    input_data = preprocess_input(departement, annee, kilometrage, gear, energy, brand, model_name)
    prediction = model.predict([input_data])
    st.write(f'The predicted price is: ${prediction[0]:,.2f}')
