import re
import os
import nltk
from  nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

stop_words=set(stopwords.words('english'))

def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z]',' ',text)
    text=re.sub(r's\+',' ',text)
    words=text.split()
    words=[word for word in words if word not in stop_words]
    return " ".join(words)

def match_resumes(job_description,resumes):
    cleaned_job=clean_text(job_description)
    cleaned_resumes=[clean_text(resume) for resume in resumes]
    documents=[cleaned_job]+cleaned_resumes
    vectorizer=TfidfVectorizer(ngram_range=(1,2),max_features=500)
    tfidf_matrix=vectorizer.fit_transform(documents)
    similarities=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:])
    scores=[round(score*100,2) for score in similarities[0]]
    return scores