import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open("fraud_model.pkl", "rb"))

# page config
st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection System")
st.markdown("### Enter transaction details below")

# inputs
time = st.number_input("⏱ Transaction Time")
amount = st.number_input("💰 Transaction Amount")

st.markdown("### 🔢 Feature Inputs")

v_inputs = []
for i in range(1, 11):
    val = st.number_input(f"V{i}")
    v_inputs.append(val)

# prediction button
if st.button("🔍 Predict"):
    features = np.array([[time, amount] + v_inputs])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.success("✅ Safe Transaction")