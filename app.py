import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("customer_churn_model.pkl")

st.title("Churn Prediction App")
st.divider()

age = st.number_input("Enter Age", 10, 100, 30)
tenure = st.number_input("Tenure (months)", 0, 72, 12)
monthlycharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict Churn"):
    gender_selected = 1 if gender == "Female" else 0
    X = np.array([[age, gender_selected, tenure, monthlycharges]])
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]

    result = "Yes" if prediction == 1 else "No"
    st.success(f"Customer likely to churn: **{result}**")
