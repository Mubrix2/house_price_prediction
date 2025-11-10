import streamlit as st
import  pandas as pd
import pickle
from feature_engineering import FeatureEngineer



@st.cache_resource
def load_model():
   with open('houseprice.pkl', 'rb') as f:
        model = pickle.load(f)
   return model

model = load_model()





st.title('House Price Prediction Model')

st.write("Enter property details to predict the estimated price:")


year_built = st.number_input("Year the house was built", 1900, 2025, 2000)
lot_area = st.number_input("Lot area (sq ft)", 100, 10000, 2000)
sqft = st.number_input("House area (sq ft)", 100, 5000, 1500)
house_type = st.selectbox("House type", ["Detached", "Semi-detached", "Apartment"])
garage = st.number_input("Number of garages", 0, 10, 1)
total_rooms = st.number_input("Total number of rooms", 1, 20, 5)

# Map to pipeline columns
input_data = pd.DataFrame({
    'Year_Built': [year_built],
    'Lot_Area': [lot_area],
    'SqFt': [sqft],
    'Type': [house_type],
    'Garage': [garage],
    'Total_rooms': [total_rooms]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")

