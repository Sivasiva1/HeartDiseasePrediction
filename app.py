import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('heartdiseasemodel.pkl','rb'))

data = pd.read_csv('heart_disease.csv')

st.header('Heart Disease Predictor')

gender = st.selectbox('Choose Gender',data['Gender'].unique())
if gender == "Male":
    gen = 1
else:
    gen = 0

age = st.number_input('Enter Age')
CuurentSmoker = st.selectbox('Patient CurrentSmoker?',data['currentSmoker'].unique())
CigsPerDay =  st.number_input('Enter CigsPerDay')
BpMeds =   st.number_input('Is patient on BpMeds')
prevalentStroke =  st.selectbox('Is Patient affected by stroke',data['prevalentStroke'].unique())
if prevalentStroke == "no":
    p = 0
else:
    p = 1
prevalentHyp =  st.selectbox('prevalentHyp Status',data['prevalentHyp'].unique())
diabetes =  st.selectbox('Diabetes Status',data['diabetes'].unique())
totchol =  st.number_input('Enter totchol')
sysBP =  st.number_input('Enter sysBP')
diaBp =  st.number_input('Enter diaBP')
BMI =  st.number_input('Enter BMI')
HeartRate =  st.number_input('Enter HeartRate')
glucose = st.number_input('Enter Glucose Level')

if st.button ('Predict'):
    input =np.array([[gen,age,CuurentSmoker,CigsPerDay,BpMeds,p,prevalentHyp,diabetes,totchol ,sysBP ,diaBp,BMI,HeartRate,glucose]])
    x = model.predict(input)

    if x[0] == 1:
        st.error("Yes,Patient may have a heart disease")
    else:
        st.success("Patient is Healthy")