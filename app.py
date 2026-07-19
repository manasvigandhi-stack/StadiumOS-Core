import streamlit as st
import json
# Import your actual agent logic here
# from agent_workflow import run_agent_process 

st.title("StadiumOS-Core: Incident Manager")
st.write("FIFA 2026 Volunteer Support System")

incident_input = st.text_area("Describe the incident:")
if st.button("Submit Report"):
    st.info("Agent is processing...")
    # result = run_agent_process(incident_input)
    st.success("Incident logged successfully!")
    # st.json(result)
