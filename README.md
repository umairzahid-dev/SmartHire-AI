# SmartHire AI - Resume Screening System

## Overview

SmartHire AI is a Resume Screening and Candidate Ranking System that automates the initial candidate evaluation process.

The system leverages Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity to compare resumes against a job description and rank candidates based on relevance.

The objective is to streamline resume screening and assist recruiters in identifying the most suitable candidates efficiently.

---

## Features

* Resume preprocessing and text normalization
* TF-IDF based document representation
* Cosine similarity based candidate ranking
* Multiple resume support
* PDF resume text extraction
* Automated resume ranking pipeline
* Deployment-ready architecture

---

## Project Workflow

```text
Job Description
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Transformation
        │
        ▼
Cosine Similarity
        │
        ▼
Candidate Ranking
        │
        ▼
Top Matching Resumes
```

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* PyMuPDF
* Joblib
* Regular Expressions (re)

### Machine Learning Techniques

* TF-IDF Vectorization
* Cosine Similarity

---

## Project Structure

```text
SmartHire-AI/

├── data/
│   ├── clean_resumes.csv
│   └── clean_jobs.csv
│
├── models/
│   └── tfidf.pkl
│
├── notebooks/
│   └── SmartHire.ipynb
│
├── app/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

```bash
git clone https://github.com/your-username/SmartHire-AI.git

cd SmartHire-AI

pip install -r requirements.txt
```

---

## Usage

1. Upload one or more resume PDFs.
2. Provide a job description.
3. Calculate similarity scores.
4. Rank candidates based on relevance.

---

## Future Enhancements

* Skill matching module
* Missing skill detection
* Candidate insights dashboard
* FastAPI integration
* Advanced NLP-based candidate analysis

---

## Learning Outcomes

This project demonstrates:

* Text preprocessing and normalization
* Feature engineering using TF-IDF
* Similarity-based document ranking
* Resume screening workflows
* Model persistence using Joblib
* End-to-end machine learning pipeline development

---

## Author

**Umair Zahid**

