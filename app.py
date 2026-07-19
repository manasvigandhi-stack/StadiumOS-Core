import streamlit as st

# Optimized for readability and professional aesthetics
st.set_page_config(page_title="StadiumOS-Core", layout="centered")

st.markdown("""
    <style>
    /* High-Contrast, Professional Background */
    .stApp {
        background: #f0f2f6; 
        background-image: radial-gradient(#d1d5db 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* Glassmorphism Card Effect for high readability */
    .main .block-container {
        background: rgba(255, 255, 255, 1);
        padding: 40px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    h1 { color: #004d26; text-align: center; font-weight: 800; }
    
    /* Button refinement for better UI */
    .stButton>button { 
        background-color: #004d26 !important; 
        color: #ffffff !important; 
        width: 100%; 
        border-radius: 8px; 
        border: none;
        padding: 12px;
        font-weight: 600;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: scale(1.02); }
    
    /* Text readability check */
    .stMarkdown, .stSelectbox, .stTextInput { color: #1f2937 !important; }
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
