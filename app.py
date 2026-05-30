import streamlit as st
import pandas as pd
from datetime import date

from database import *
from ai_prediction import predict_health

create_table()

st.title("Health Prediction Application")

st.subheader("Add Patient")

name = st.text_input("Full Name")

dob = st.date_input(
    "Date of Birth",
    max_value=date.today()
)

email = st.text_input("Email Address")

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

if st.button("Save Patient"):

    if name == "":
        st.error("Enter Name")

    elif "@" not in email:
        st.error("Invalid Email")

    else:

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient(
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Patient Saved")

st.divider()

st.subheader("Patient Records")

records = get_patients()

if records:

    df = pd.DataFrame(
        records,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df)

st.divider()

st.subheader("Delete Patient")

patient_id = st.number_input(
    "Patient ID",
    min_value=1
)

if st.button("Delete"):
    delete_patient(patient_id)
    st.success("Patient Deleted")
