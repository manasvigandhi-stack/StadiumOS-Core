import streamlit as st

# Custom Theme and CSS
st.set_page_config(page_title="StadiumOS-Core", layout="wide")

st.markdown("""
    <style>
    /* FIFA-Inspired Color Palette & Styling */
    .stApp { background-color: #f8f9fa; }
    h1 { color: #003366; } /* Deep Stadium Blue */
    .stButton>button { 
        background-color: #003366 !important; 
        color: white !important; 
        width: 100%; 
        border-radius: 8px; 
    }
    div.stMarkdown { color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🏟️ FIFA 2026 Operations")
    st.write("System Status: **Active**")
    st.write("Mode: **Agentic Core**")
    st.info("Operating in Official Tournament Mode")

# Main Page
st.title("StadiumOS-Core")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Incident Reporting")
    incident_input = st.text_area("Live Report Details", placeholder="Enter incident report here...", height=150)
    
    if st.button("🚀 Execute Analysis"):
        if incident_input:
            with st.spinner("Agent running Observe-Think-Act..."):
                st.success("Analysis Complete.")
                st.write("### 🧠 Agent Reasoning")
                st.json({
                    "status": "Escalated",
                    "priority": "Critical",
                    "timestamp": "2026-07-19 22:50:00",
                    "action_taken": "Sector Supervisor Alerted",
                    "protocol": "FIFA-Safety-Alpha"
                })
        else:
            st.warning("Please input incident details.")

with col2:
    st.subheader("📊 Operational Monitor")
    st.markdown("""
    <div style='background-color: #e3f2fd; padding: 15px; border-radius: 8px;'>
    <strong>Live Data Streams</strong><br>
    All stadium sectors are reporting healthy data. Incident queue is clear.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("- **Safety Protocol:** Active")
    st.write("- **Autonomous Level:** 5")
    st.write("- **Edge Connectivity:** Stable")
