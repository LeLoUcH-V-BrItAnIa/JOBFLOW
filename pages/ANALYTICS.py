import streamlit as st
import pandas as pd
import plotly.express as px

from services.analytics_service import get_status_counts

st.title("📊 Analytics")

counts = get_status_counts()

df = pd.DataFrame(
    {
        "Status": counts.keys(),
        "Count": counts.values()
    }
)

fig = px.pie(
    df,
    names="Status",
    values="Count",
    title="Applications By Status"
)

st.plotly_chart(fig)