import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Used Car Price Prediction", page_icon="🚗")

st.title("🚗 Used Car Price Prediction")
st.write("Enter car details below to predict the selling price.")

# User inputs
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2026, value=2015)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=50000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox(
    "Owner Type",
    ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"]
)

# Encoding same as notebook
fuel_map = {
    "Petrol": 0,
    "Diesel": 1,
    "CNG": 2,
    "LPG": 3,
    "Electric": 4
}

seller_map = {
    "Dealer": 0,
    "Individual": 1,
    "Trustmark Dealer": 2
}

transmission_map = {
    "Manual": 0,
    "Automatic": 1
}

owner_map = {
    "First Owner": 0,
    "Second Owner": 1,
    "Third Owner": 2,
    "Fourth & Above Owner": 3,
    "Test Drive Car": 4
}

car_age = 2026 - year

# Important: order must match training features
input_data = pd.DataFrame({
    "km_driven": [km_driven],
    "fuel": [fuel_map[fuel]],
    "seller_type": [seller_map[seller_type]],
    "transmission": [transmission_map[transmission]],
    "owner": [owner_map[owner]],
    "car_age": [car_age]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)

    st.success(f"Estimated Selling Price: ₹ {prediction[0]:,.2f}")