import streamlit as st

# FIFA/Football Inspired Styling
st.set_page_config(page_title="StadiumOS-Core", layout="wide")

st.markdown("""
    <style>
    /* Stadium & Pitch Inspired Palette */
    .stApp { background-color: #f0f7f4; }
    h1 { color: #004d26; text-align: center; } /* Pitch Green */
    .stButton>button { background-color: #004d26 !important; color: white !important; font-weight: bold; border-radius: 20px; }
    
    /* Animation for smooth feel */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .main { animation: fadeIn 1s ease-in; }
    
    .stAlert { border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ StadiumOS-Core: Live Ops")

# Dropdown for rapid reporting
incident_type = st.selectbox(
    "Select Incident Type (Quick Report):",
    ["Select...", "Missing Child", "Medical Emergency", "Security Concern", "Accessibility Issue", "Other"]
)

# Conditional text area
incident_details = ""
if incident_type == "Other":
    incident_details = st.text_area("Provide details:")
elif incident_type != "Select...":
    st.info(f"System ready to log: {incident_type}")
    incident_details = st.text_input("Additional notes (Optional):")

# Logic
if st.button("Submit Report"):
    if incident_type == "Select...":
        st.warning("Please select an incident type.")
    else:
        with st.spinner("Processing through Agentic Core..."):
            st.success(f"Report Logged: {incident_type}")
            st.json({
                "Incident": incident_type,
                "Priority": "High" if incident_type in ["Missing Child", "Medical Emergency"] else "Medium",
                "Status": "Dispatched to Sector Lead",
                "Timestamp": "2026-07-19 23:10:00"
            })
