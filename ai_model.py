import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_jobs(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'jobs.json')
    with open(path, 'r') as f:
        return json.load(f)

def recommend_jobs(user_input, top_n=3):
    jobs = load_jobs()
    documents = [job['description'] + ' ' + ' '.join(job['skills']) for job in jobs]
    documents.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    scores = cosine_sim[0].argsort()[::-1][:top_n]

    return [jobs[i] for i in scores]
