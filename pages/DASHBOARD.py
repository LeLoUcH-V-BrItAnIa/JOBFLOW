import streamlit as st

from services.job_service import get_all_jobs,get_job_stats,delete_job,search_job,update_job_status

st.title("DASHBOARD")
jobs = get_all_jobs()
stats = get_job_stats()
status_filter = st.selectbox(
    "Filter Status",
    options=[
        "All",
        "Applied",
        "Interview",
        "Accepted",
        "Rejected"
    ]
)
if status_filter!= "All":
    jobs = [job for job in jobs if job.get("status")==status_filter]
search_text = st.text_input("Search Company")
if search_text:
    jobs = search_job(search_text)
else:
    jobs = get_all_jobs()
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Jobs",
    stats["total"]
)

col2.metric(
    "Applied",
    stats["applied"]
)

col3.metric(
    "Interview",
    stats["interview"]
)

col4.metric(
    "Accepted",
    stats["accepted"]
)
if not jobs:
    st.warning("No jobs found")
else:
    for job in jobs:
        with st.container(border=True):

            st.subheader(
                job.get("company_name")
            )

            st.write(
                f"💼 {job.get('role')}"
            )

            st.write(
                f"🔥 {job.get('priority')}"
            )

            st.write(
                f"📝 {job.get('notes')}"
            )
            st.write(
                f"📅 {job.get('application_date','N/A')}"
            )

            st.write(
                f"📍 {job.get('location')}"
            )

            st.write(
                f"🔗 {job.get('job_link','N/A')}"
            )
            status = job.get("status")
            if status == "Accepted":
                st.success(status)

            elif status == "Rejected":
                st.error(status)

            elif status == "Interview":
                st.warning(status)

            else:
                st.info(status)
            new_status = st.selectbox("Change Stuatus",
                        options=[
                            "Applied",
                            "Interview",
                            "Accepted",
                            "Rejected"
                            ],
                        key = f"status_select{job['_id']}"
                            )
            if st.button("Update Status",key = f"status_{job['_id']}"):
                update_job_status(str(job["_id"]),new_status)
                st.rerun()
            if st.button("DELETE",key=str(job["_id"])):
                delete_job(str(job["_id"]))
                st.rerun()
