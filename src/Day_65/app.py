import streamlit as st
import joblib
import numpy as np

st.title("Student Performance Predictor")

try:
    model = joblib.load("model.pkl")
except:
    st.error("Model file not found!")
    st.stop()

input1 = st.number_input("Enter Study Hours")
input2 = st.number_input("Enter Attendance")

if st.button("Predict"):
    prediction = model.predict([[input1, input2]])
    st.success(f"Predicted Score: {prediction[0]}")