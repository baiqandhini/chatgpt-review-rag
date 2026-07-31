import os
import urllib.request

import numpy as np
import pandas as pd

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer

import google.generativeai as genai


# =====================================================
# Load Environment
# =====================================================

load_dotenv()

try:
    import streamlit as st

    GEMINI_API_KEY = st.secrets.get(
        "GEMINI_API_KEY",
        os.getenv("GEMINI_API_KEY")
    )

except Exception:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY tidak ditemukan. "
        "Pastikan file .env (lokal) atau Streamlit Secrets sudah benar."
    )

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-3.6-flash"
)

# =====================================================
# Download Embeddings (if not exists)
# =====================================================
import gdown

EMBEDDING_FILE = "review_embeddings.npy"
EMBEDDING_ID = "1EkgK4xHvIrxXTem5IPU_xv71euVm-MzZ"


def download_embeddings():

    if not os.path.exists(EMBEDDING_FILE):

        print("Downloading review embeddings...")

        gdown.download(f"https://drive.google.com/uc?id={EMBEDDING_ID}", EMBEDDING_FILE, quiet=False)

        print("Download completed.")


download_embeddings()


# =====================================================
# Load Dataset
# =====================================================

reviews = pd.read_csv("processed_reviews.csv")

embeddings = np.load(EMBEDDING_FILE)


# =====================================================
# Load Embedding Model
# =====================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =====================================================
# Retrieval Function
# =====================================================

def retrieve_reviews(query, top_k=5):

    query_embedding = embedding_model.encode([query])

    similarity = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_idx = np.argsort(similarity)[::-1][:top_k]

    retrieved = reviews.iloc[top_idx].copy()

    retrieved["Similarity"] = similarity[top_idx]

    return retrieved


# =====================================================
# Answer Generation
# =====================================================

def answer_question(question, top_k=5):

    retrieved = retrieve_reviews(question, top_k)

    context = ""

    for _, row in retrieved.iterrows():

        context += f"""
Review:
{row['Comment']}

Rating:
{row['Rating']}

Sentiment:
{row['Sentiment']}

"""

    prompt = f"""
You are an AI assistant.

Use ONLY the reviews provided below to answer the user's question.

If the reviews do not contain enough information,
respond with:

"The available reviews do not provide enough information to answer this question."

Reviews:

{context}

Question:

{question}

Provide a concise and factual answer.
"""

    response = model.generate_content(prompt)

    return response.text, retrieved


if __name__ == "__main__":

    answer, refs = answer_question(
        "Why do users like ChatGPT?"
    )

    print(answer)