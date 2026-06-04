import streamlit as st
from database.pymongo_db import db
from services.job_service import create_job

st.title("ADD JOB")
try:
    db.command("ping")
    st.success("MongoDB connected Successfully!")
    # main code 
    company_name = st.text_input("Company Name")
    status = st.selectbox(
        "Status",
        options=[
                    "Applied",
                    "Assessment",
                    "Interview",
                    "HR Round",
                    "Accepted",
                    "Rejected"
                ]
        )
    priority = st.selectbox(
        "priority",
        options=[
        "Low",
        "Medium",
        "High"
    ])
    notes = st.text_area("Notes")
    role = st.text_input("Role")
    application_date = st.date_input(
        "Application Date"
    )

    job_link = st.text_input(
        "Job Link"
    )

    location = st.text_input(
        "Location"
    )
    if st.button("SAVE JOB"):
        job_id = create_job(company_name,role,status,priority,notes,application_date,job_link,location)
        st.success(f"job saved successfully!")
        st.write("MongoDB ID",job_id)
        st.write(role)
except Exception as e:
    st.error(f"Connection Filed: {e}")