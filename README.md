# resume-screening-nlp
NLP-based resume screening system using TF-IDF and Flask API

# Resume Screening System using NLP

## Overview
This project automates resume screening by matching resumes against a job description using Natural Language Processing techniques.

## Features
- Text preprocessing (cleaning, stopword removal)
- TF-IDF vectorization with bigrams
- Cosine similarity-based matching
- Resume ranking
- Flask REST API

## Tech Stack
- Python
- NLP
- Scikit-learn
- Flask
- NLTK

## API Endpoint

### POST /match

**Request Body**
```json
{
  "job_description": "Looking for a Python developer with ML and NLP experience",
  "resumes": [
    "Python developer skilled in pandas numpy machine learning",
    "Data analyst experienced in Excel SQL"
  ]
}

## How to Run

```bash
pip install -r requirements.txt
python app.py



