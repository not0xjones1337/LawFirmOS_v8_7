import streamlit as st
from core import summarize, draft_motion
from ingest import ingest

st.title("Law Firm OS v8.4 — Enterprise Litigation System")

case_id = st.text_input("Case ID")

if st.button("Ingest Case"):
    st.write(ingest(case_id))

query = st.text_input("Legal Query")

if st.button("Summarize"):
    st.write(summarize(case_id, query))

motion = st.text_input("Motion Type")

if st.button("Draft Motion"):
    st.write(draft_motion(case_id, motion))

