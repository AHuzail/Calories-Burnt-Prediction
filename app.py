import pickle
import pandas as pd
import streamlit as st
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))


def predict_calories(data):
    prediction = model.predict(data)[0]
    return prediction


st.title("Calorie Burnt Prediction")

age = st.number_input("Age")
gender = st.selectbox("Gender", ['Male', 'Female'])
if gender == 'Male':
    gender = 0
else:
    gender = 1
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Exercise Duration (minutes)")
body_temp = st.number_input("Body Temperature")
heart_rate = st.number_input("Heart Rate")

data = pd.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
data = np.vstack(data)

# Button to make prediction
if st.button("Predict Calories Burnt"):
    calories = predict_calories(data)
    st.success(f"Estimated Calories Burnt: {calories:.2f}")
