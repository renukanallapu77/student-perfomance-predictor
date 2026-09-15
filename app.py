import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Student Performance Predictor - By Renuka")

st.title("🎓 Student Performance Predictor")
st.write("Built by Renuka Nallapu | SVIST | CGPA 8.6")

# Input
hours = st.slider("Study Hours per Day", 1, 10, 5)
attendance = st.slider("Attendance %", 40, 100, 75)
prev_cgpa = st.slider("Previous CGPA", 5.0, 10.0, 8.6)

# Simple Logic (We will train ML model tomorrow)
if hours >= 6 and attendance >= 75:
    result = "High Performer - 9+ CGPA Expected!"
    color = "green"
elif hours >= 4:
    result = "Average - 7-8 CGPA Expected"
    color = "orange"
else:
    result = "Needs Improvement"
    color = "red"

if st.button("Predict"):
    st.markdown(f":{color}[{result}]")
    st.balloons()
    st.write(f"Your input matches my journey: I studied {hours} hrs, got 8.6 CGPA!")

st.caption("Day 6/30 - Building in Public - SVIST CP Lab")
