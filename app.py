import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open('lrmodel_sustainability.pkl', 'rb') as file:
    model = pickle.load(file)

#Title for your application
st.title("Sustainable Checker")

#User inputs
carbon_emissions = st.number_input("Carbon Emissions (in tons)", min_value=0.0, format="%f")
energy_output = st.number_input("Energy Output (in MWh)", min_value=0.0, format="%f")
renewability_index = st.number_input("Renewability Index (0-100)", min_value=0.0, format="%f")
cost_efficiency = st.number_input("Cost Efficiency (in $/MWh)", min_value=0.0, format="%f")

#Prediction button
if st.button("Check Sustainability"):
    # Prepare the input data for prediction
    input_data = np.array([[carbon_emissions, energy_output, renewability_index, cost_efficiency]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.success("The energy source is Sustainable.")
    else:
        st.info("The energy source is Not Sustainable.")