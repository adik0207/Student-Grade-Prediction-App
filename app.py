import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Load model, encoders, and column names
model = joblib.load("grade_predictor.pkl")
with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)
with open("columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.set_page_config(page_title="Student Grade Predictor")
st.title("📘 Student Grade Predictor (G3)")

st.markdown("Please answer the following questions about the student:")

# Function to encode a single input row
def encode_input(user_input, encoders):
    for col in user_input.columns:
        if col in encoders:
            le = encoders[col]
            try:
                user_input[col] = le.transform(user_input[col])
            except ValueError:
                user_input[col] = le.transform([le.classes_[0]])[0]  # default to first known value
    return user_input

# ---- User Inputs (simple and friendly) ----
sex = st.selectbox("Gender", ["female", "male"])
address = st.selectbox("Home Location", ["Urban", "Rural"])
famsize = st.selectbox("Family Size", ["More than 3", "3 or less"])
Pstatus = st.selectbox("Parent Status", ["Living together", "Apart"])

Medu = st.slider("Mother's Education Level (0 - none to 4 - higher)", 0, 4, 2)
Fedu = st.slider("Father's Education Level (0 - none to 4 - higher)", 0, 4, 2)

studytime = st.slider("Weekly Study Time (1 - <2h to 4 - >10h)", 1, 4, 2)
failures = st.slider("Past Class Failures", 0, 3, 0)
absences = st.slider("Number of School Absences", 0, 93, 4)

G1 = st.slider("First Period Grade (0–20)", 0, 20, 10)
G2 = st.slider("Second Period Grade (0–20)", 0, 20, 10)

# Collect into DataFrame
input_dict = {
    'sex': [sex],
    'address': [address],
    'famsize': [famsize],
    'Pstatus': [Pstatus],
    'Medu': [Medu],
    'Fedu': [Fedu],
    'studytime': [studytime],
    'failures': [failures],
    'absences': [absences],
    'G1': [G1],
    'G2': [G2]
}

# Add remaining required columns with default values (optional)
# This step depends on what columns were used during training
# Here we just add missing ones as placeholder
for col in model_columns:
    if col not in input_dict:
        input_dict[col] = [0]  # default placeholder

input_df = pd.DataFrame(input_dict)
input_df = input_df[model_columns]  # ensure correct order

# Encode object type columns
input_df = encode_input(input_df, encoders)

# Predict
if st.button("Predict Final Grade"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎓 The predicted final grade (G3) is: **{round(prediction, 2)}** out of 20.")
