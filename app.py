# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the pre-trained model
model = joblib.load('deformation_prediction_model.pkl')

# Streamlit app title
st.title("Deformation Prediction App")
st.write("This app predicts deformation based on input parameters such as load, material properties, and geometry.")

# Collect user input for each feature
def user_input_features():
    
    load = st.number_input("Load (in Newtons)", min_value=0.0, step=0.1)
    material_density = st.number_input("Material Density (kg/m^3)", min_value=0.0, step=0.1)
    youngs_modulus = st.number_input("Young's Modulus (GPa)", min_value=0.0, step=0.1)
    length = st.number_input("Length (in meters)", min_value=0.0, step=0.01)
    width = st.number_input("Width (in meters)", min_value=0.0, step=0.01)
    height = st.number_input("Height (in meters)", min_value=0.0, step=0.01)
    
    # Create a DataFrame for input
    input_data = pd.DataFrame({
        'Load': [load],
        'Material Density': [material_density],
        "Young's Modulus": [youngs_modulus],
        'Length': [length],
        'Width': [width],
        'Height': [height]
    })
    return input_data

# input
input_df = user_input_features()

# Button to perform prediction
if st.button("Predict Deformation"):
    # Perform prediction using the input data
    prediction = model.predict(input_df)
    st.write(f"Predicted Deformation: {prediction[0]:.4f} units")
