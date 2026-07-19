import streamlit as st

# Configure the page for a professional look
st.set_page_config(page_title="StadiumOS-Core", layout="wide")

# Sidebar for metadata
with st.sidebar:
    st.title("⚙️ System Status")
    st.write("Status: **Active**")
    st.write("Mode: **Agentic Core**")
    st.divider()
    st.write("FIFA 2026 Operations")

# Main Interface
st.title("🏟️ StadiumOS-Core")
st.subheader("Autonomous Incident Management System")

# Layout: Two columns for a balanced UI
col1, col2 = st.columns([2, 1])

with col1:
    incident_input = st.text_area("Incident Description", placeholder="e.g., A child is missing in Sector 104...")
    if st.button("🚀 Process Incident"):
        if incident_input:
            with st.spinner("Agent is running Observe-Think-Act loop..."):
                # Your logic integration here
                st.success("Incident Logged & Escalated.")
                st.write("### Agent Analysis")
                st.json({
                    "status": "Escalated",
                    "priority": "High",
                    "action": "Alerting Sector Supervisor"
                })
        else:
            st.warning("Please enter an incident description.")

with col2:
    st.markdown("### 📊 Operational Overview")
    st.info("The system is currently monitoring real-time data from all stadium sectors.")
    st.write("- **Safety Protocol:** Enabled")
    st.write("- **Escalation Mode:** Automatic")
    st.write("- **Network Status:** Local-First Active")
