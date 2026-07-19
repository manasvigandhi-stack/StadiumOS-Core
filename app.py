import streamlit as st

# FIFA-Inspired Polished Layout
st.set_page_config(page_title="StadiumOS-Core", layout="centered")

st.markdown("""
    <style>
    /* Animated Gradient Background - Stadium Night Theme */
    .stApp {
        background: linear-gradient(-45deg, #004d26, #003366, #1a1a1a, #004d26);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        height: 100vh;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Content Card */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    h1 { color: #004d26; text-align: center; }
    .stButton>button { background-color: #004d26 !important; color: white !important; width: 100%; border-radius: 10px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Main App Content
st.title("⚽ StadiumOS-Core")
st.subheader("Live Operations Dashboard", anchor=False)

incident_type = st.selectbox(
    "Select Incident Type:",
    ["Select...", "Missing Child", "Medical Emergency", "Security Concern", "Accessibility Issue", "Other"]
)

if incident_type != "Select...":
    st.info(f"System ready to log: {incident_type}")
    incident_details = st.text_input("Additional notes (Optional):")

    if st.button("Submit Report"):
        with st.spinner("Processing Agentic Logic..."):
            st.success(f"Report Logged Successfully")
            st.json({
                "Type": incident_type,
                "Priority": "High",
                "Status": "Dispatched"
            })
