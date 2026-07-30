import re
import fitz
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):

    text = str(text)

    text = re.sub(r"http\S+|www\S+", " ", text)

    text = re.sub(r"\S+@\S+", " ", text)

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    text = text.lower()

    text = re.sub(r"\s+", " ", text).strip()

    return text


def extract_text_from_pdf(pdf_file):

    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:

        text += page.get_text()

    pdf.close()

    return text


def analyze_uploaded_resumes(uploaded_files, job_text, tfidf):

    resumes = []

    for file in uploaded_files:

        resume_text = extract_text_from_pdf(file)

        clean_resume = clean_text(resume_text)

        resumes.append({
            "Resume": file.name,
            "clean_resume": clean_resume
        })

    resume_df = pd.DataFrame(resumes)

    resume_vectors = tfidf.transform(resume_df["clean_resume"])

    job_vector = tfidf.transform([clean_text(job_text)])

    scores = cosine_similarity(job_vector, resume_vectors).flatten()

    resume_df["Match Score"] = (scores * 100).round(2)

    resume_df = resume_df.sort_values(
        "Match Score",
        ascending=False
    )

    return resume_df.head(10)