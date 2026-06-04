import streamlit as st
from services.job_service import get_all_jobs

st.title("📌 JobFlow Kanban Board")

jobs = get_all_jobs()
col1, col2, col3, col4, col5 = st.columns([1,1.2,1,1,1])
col1.subheader("📨 Applied")
col2.subheader("📝 Assessment")
col3.subheader("🎤 Interview")
col4.subheader("✅ Accepted")
col5.subheader("❌ Rejected")
for job in jobs:

    status = job.get("status")

    if status == "Applied":
        current_col = col1

    elif status == "Assessment":
        current_col = col2

    elif status == "Interview":
        current_col = col3

    elif status == "Accepted":
        current_col = col4

    elif status == "Rejected":
        current_col = col5

    else:
        continue

    with current_col:

        with st.container(border=True):

            st.write(
                f"**{job.get('company_name')}**"
            )

            st.caption(
                job.get("role")
            )

            st.write(
                job.get("priority")
            )