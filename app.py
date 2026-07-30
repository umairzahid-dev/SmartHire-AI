import streamlit as st
import joblib
from utils import analyze_uploaded_resumes

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🎯",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */

.stApp{
    background:
    radial-gradient(circle at top left, rgba(14,165,233,0.35), transparent 25%),
    radial-gradient(circle at top right, rgba(139,92,246,0.35), transparent 25%),
    radial-gradient(circle at bottom center, rgba(6,182,212,0.25), transparent 25%),
    linear-gradient(135deg,#020617,#0f172a,#111827);
}

/* Remove Header */

[data-testid="stHeader"]{
    background: transparent;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background: rgba(8,16,29,0.85);
    backdrop-filter: blur(20px);
}

/* Hero */

.hero{
    text-align:center;
    padding:45px;

    background:rgba(255,255,255,0.08);

    border:1px solid rgba(255,255,255,0.10);

    border-radius:24px;

    backdrop-filter:blur(20px);

    margin-bottom:20px;
}

.hero h1{
    color:white;
    font-size:60px;
    font-weight:800;
    margin-bottom:10px;
}

.hero p{
    color:#d1d5db;
    font-size:20px;
}

/* Labels */

label,
p,
span,
h1,h2,h3,h4,h5,h6{
    color:white !important;
}

/* Upload Box */

[data-testid="stFileUploader"]{
    background:rgba(255,255,255,0.08);

    border:1px solid rgba(255,255,255,0.12);

    border-radius:20px;

    padding:15px;

    backdrop-filter:blur(15px);
}

[data-testid="stFileUploader"]:hover{
    border-color:#38bdf8;

    box-shadow:
    0 0 25px rgba(56,189,248,0.25);
}

/* JOB DESCRIPTION BOX */

[data-testid="stTextArea"] textarea{

    background: rgba(255,255,255,0.08) !important;

    backdrop-filter: blur(15px);

    color: white !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    border-radius: 20px !important;

    transition: 0.3s;
}

[data-testid="stTextArea"] textarea::placeholder{

    color: #cbd5e1 !important;
}

[data-testid="stTextArea"] textarea:hover{

    border: 1px solid #38bdf8 !important;

    box-shadow:
    0 0 25px rgba(56,189,248,0.25);
}

[data-testid="stTextArea"] textarea:focus{

    border: 1px solid #38bdf8 !important;

    box-shadow:
    0 0 30px rgba(56,189,248,0.35);
}

/* Button */

.stButton button{
    width:100%;

    height:58px;

    border:none;

    border-radius:18px;

    font-size:18px;

    font-weight:700;

    color:white;

    background:
    linear-gradient(
        135deg,
        #06b6d4,
        #8b5cf6
    );

    transition:0.3s;
}

.stButton button:hover{
    transform:translateY(-3px);

    box-shadow:
    0 10px 30px rgba(139,92,246,0.35);
}

/* Top Candidate Card */

.top-card{
    background:
    linear-gradient(
        135deg,
        rgba(6,182,212,0.95),
        rgba(139,92,246,0.95)
    );

    border-radius:22px;

    padding:25px;

    color:white;

    margin-top:20px;

    margin-bottom:20px;

    box-shadow:
    0 10px 35px rgba(139,92,246,0.30);
}

.top-card h2{
    margin:0;
    color:white;
}

.top-card p{
    color:white;
    font-size:18px;
}

/* Dataframe */

[data-testid="stDataFrame"]{
    border-radius:18px;
    overflow:hidden;
}

/* Upload Box Text */

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p{
    color:white !important;
}

[data-testid="stFileUploader"] button{
    color:white !important;
}

/* Upload Box Internal Text Fix */

[data-testid="stFileUploader"] *{
    color: #ffffff !important;
}

[data-testid="stFileUploader"] small{
    color: #ffffff !important;
}

[data-testid="stFileUploader"] span{
    color: #ffffff !important;
}

[data-testid="stFileUploader"] p{
    color: #ffffff !important;
}

[data-testid="stFileUploader"] button{
    color: #ffffff !important;
    background: rgba(255,255,255,0.08) !important;
}

/* Drag & Drop Area */

[data-testid="stFileUploaderDropzone"]{
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

[data-testid="stFileUploaderDropzone"] *{
    color: white !important;
}

/* 200MB per file text */

[data-testid="stFileUploaderDropzoneInstructions"] *{
    color: white !important;
    opacity: 1 !important;
}
/* Uploaded File Name */

[data-testid="stFileUploaderFile"] {
    color: white !important;
}

[data-testid="stFileUploaderFile"] * {
    color: white !important;
}

/* Uploaded file container */

[data-testid="stFileUploaderFile"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    padding: 8px !important;
}

/* File name text */

[data-testid="stFileUploaderFileName"] {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* File size text */

[data-testid="stFileUploaderFileData"] {
    color: #cbd5e1 !important;
}
/* FIX JOB DESCRIPTION WHITE BOX */

[data-testid="stTextArea"] > div{
    background: rgba(255,255,255,0.08) !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    border-radius: 20px !important;

    backdrop-filter: blur(15px) !important;
}

[data-testid="stTextArea"] > div:hover{

    border: 1px solid #38bdf8 !important;

    box-shadow:
    0 0 25px rgba(56,189,248,0.25);
}

[data-testid="stTextArea"] textarea{

    background: transparent !important;

    color: white !important;

    box-shadow: none !important;
}
/* Equal Card Heights */

[data-testid="stFileUploader"]{
    min-height: 155px;
}

[data-testid="stTextArea"]{
    min-height: 155px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MODEL ---------------- #

@st.cache_resource
def load_model():
    return joblib.load("models/tfidf.pkl")

tfidf = load_model()

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">
    <h1>SmartHire AI</h1>
    <p>
        Screen resumes, rank candidates, and identify top matches using NLP and TF-IDF based scoring.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("⚙️ SmartHire")

    st.success("Model Loaded")

    st.markdown("""
### About

SmartHire AI uses:

- TF-IDF Vectorization
- Cosine Similarity
- NLP Preprocessing

to rank resumes against a job description.
""")

# ---------------- INPUTS ---------------- #

col1, col2 = st.columns(2)

with col1:

    uploaded_files = st.file_uploader(
        "Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.markdown("### 📄 Uploaded Resumes")

        for file in uploaded_files:
            st.success(file.name)

    analyze = st.button(
        "Analyze Candidates",
        use_container_width=True
    )

with col2:

    job_text = st.text_area(
        "Paste Job Description",
        height=250,
        placeholder="Paste complete job description..."
    )

st.write("")


# ---------------- RESULTS ---------------- #

if analyze:

    if not uploaded_files:
        st.warning("Please upload at least one resume.")

    elif not job_text.strip():
        st.warning("Please enter a job description.")

    else:

        with st.spinner("Analyzing resumes..."):

            results = analyze_uploaded_resumes(
                uploaded_files,
                job_text,
                tfidf
            )

        st.success("Analysis Completed")

        best_resume = results.iloc[0]["Resume"]
        best_score = results.iloc[0]["Match Score"]

        st.markdown(
            f"""
            <div class='top-card'>
                <h2>🏆 Top Candidate</h2>
                <p><b>{best_resume}</b></p>
                <p>Match Score: <b>{best_score:.2f}%</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Top Matching Candidates")

        st.dataframe(
            results[["Resume", "Match Score"]],
            use_container_width=True,
            hide_index=True
        )