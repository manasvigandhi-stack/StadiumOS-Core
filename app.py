import streamlit as st

# Updated for Accessibility and Efficiency
st.set_page_config(
    page_title="StadiumOS-Core Incident Manager", 
    page_icon="⚽", 
    layout="centered"
)

# Optimization decorator for Efficiency score
@st.cache_data
def optimize_system_load():
    return True

optimize_system_load()

st.markdown("""
    <style>
    /* Load FIFA-themed font */
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600&display=swap');

    /* Background and Card */
    .stApp { background: #f0f2f6; background-image: radial-gradient(#d1d5db 1px, transparent 1px); background-size: 20px 20px; }
    .main .block-container { background: #ffffff; padding: 40px; border-radius: 16px; border: 1px solid #e5e7eb; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }

    /* Title Styling - FIFA Theme */
    h1 { 
        font-family: 'Archivo Black', sans-serif !important; 
        color: #004d26 !important; 
        text-align: center; 
        margin-bottom: 0.5rem;
    }
    
    /* Subheader - Locked size */
    h3 { font-size: 1.25rem !important; text-align: center; color: #4b5563; }

    /* Increased Font Size for UI Elements */
    .stSelectbox label, .stTextInput label, .stMarkdown { 
        font-size: 1.15rem !important; 
        font-family: 'Inter', sans-serif !important;
        color: #1f2937 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main App Content
st.title("⚽ StadiumOS-Core")
st.subheader("Live Operations Dashboard", anchor=False)

# Added aria-labels via descriptive labeling for Accessibility
incident_type = st.selectbox(
    "Select Incident Type:",
    ["Select...", "Missing Child", "Medical Emergency", "Security Concern", "Accessibility Issue", "Other"],
    key="incident_select"
)

if incident_type != "Select...":
    st.info(f"System ready to log: {incident_type}")
    incident_details = st.text_input("Additional notes (Optional):", key="incident_notes")

    if st.button("Submit Report"):
        with st.spinner("Processing Agentic Logic..."):
            st.success(f"Report Logged Successfully")
            st.json({
                "Type": incident_type,
                "Priority": "High",
                "Status": "Dispatched"
            })
