# SmartHire AI

An AI Resume Screening & Candidate Ranking System built using TF-IDF and Cosine Similarity.

**Live Application:**  
https://smarthireats.streamlit.app/

---

## Overview

SmartHire AI helps recruiters and hiring teams quickly identify the most relevant candidates by comparing uploaded resumes against a job description.

The system uses Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity to rank candidates based on textual relevance.

---

## Features

- Upload multiple PDF resumes
- Paste any job description
- Automatic PDF text extraction
- Resume ranking based on relevance
- TF-IDF vectorization
- Cosine Similarity matching
- Interactive Streamlit dashboard
- Real-time candidate analysis
- Modern Glassmorphism UI

---

## Tech Stack

### Machine Learning & NLP
- Python
- Scikit-Learn
- TF-IDF Vectorizer
- Cosine Similarity

### Data Processing
- Pandas
- NumPy
- PyMuPDF

### Frontend
- Streamlit

---

## Project Workflow

1. Upload one or more resumes.
2. Enter a job description.
3. Resume text is extracted from PDF files.
4. Text is cleaned and processed.
5. TF-IDF converts text into numerical vectors.
6. Cosine Similarity compares resumes with the job description.
7. Candidates are ranked by relevance score.
8. Results are displayed in an interactive dashboard.

---

## How It Works

### TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts text into numerical vectors.

- Important keywords receive higher weights.
- Common words receive lower weights.
- Helps identify meaningful skills and job-related terms.

### Cosine Similarity

Cosine Similarity measures how similar two text vectors are.

- Score near **1.0** → Strong Match
- Score near **0.0** → Weak Match

Each uploaded resume is compared with the job description, and candidates are ranked accordingly.

---

## Future Improvements

- Skills Extraction
- Missing Skills Detection
- ATS Score Analysis
- Resume Categorization
- FastAPI Integration
- Recruiter Dashboard

---

## Author
**Umair Zahid**
