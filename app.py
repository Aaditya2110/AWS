import streamlit as st
import joblib
import numpy as np

# 1. Load the trained polynomial model
#    Make sure 'electricity_poly_model.pkl' is in the same folder or provide a full path
model = joblib.load('electricity_poly_model.pkl')

# 2. Title for the app
st.title("Electricity Bill Prediction (Polynomial Regression)")

st.markdown("""
Enter the following values to predict the Electricity Bill (excluding Month):
- Refrigerator
- AirConditioner
- Television
- Monitor
- MotorPump
- Fan
- MonthlyHours
- TariffRate
""")

# 3. Create input widgets (excluding Month)
refrigerator = st.number_input("Refrigerator (float)", min_value=0.0, value=1.0)
air_conditioner = st.number_input("AirConditioner (float)", min_value=0.0, value=1.0)
television = st.number_input("Television (float)", min_value=0.0, value=1.0)
monitor = st.number_input("Monitor (float)", min_value=0.0, value=1.0)
motor_pump = st.number_input("MotorPump (float)", min_value=0.0, value=1.0)
fan = st.number_input("Fan (float)", min_value=0.0, value=1.0)
monthly_hours = st.number_input("MonthlyHours (float)", min_value=0.0, value=100.0)
tariff_rate = st.number_input("TariffRate (float)", min_value=0.0, value=5.0)

# 4. Button to make a prediction
if st.button("Predict"):
    # Create a features list in the same order used during training
    features_list = [
        refrigerator,
        air_conditioner,
        television,
        monitor,
        motor_pump,
        fan,
        monthly_hours,
        tariff_rate
    ]
    
    # Convert to a 2D NumPy array for prediction
    input_array = np.array(features_list).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    
    st.success(f"Predicted Electricity Bill: {prediction:.2f}")
