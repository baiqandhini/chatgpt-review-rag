**ChatGPT Review RAG System**

**Overview**

This project implements a Retrieval-Augmented Generation (RAG) system for Question Answering using 100,000 ChatGPT user reviews collected from the Google Play Store.

The system retrieves the Top-5 most relevant reviews using semantic similarity based on Sentence Transformers and generates factual answers using Google Gemini. Responses are generated only from the retrieved reviews, ensuring evidence-based question answering.

**Features**

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search using Sentence Transformers

✅ Google Gemini Integration

✅ Streamlit Web Interface

✅ Automatic Embedding Download from Google Drive

✅ Evidence-based Answers

**Dataset**

Source

Google Play Store

Application

ChatGPT

Number of Reviews

100,000

Embedding Model

SentenceTransformer

all-MiniLM-L6-v2

Embedding Dimension

384

**Methodology**

The proposed system consists of four main stages.

1. Dataset Preparation

2. Sentence Embedding

3. Semantic Retrieval

4. Answer Generation using Google Gemini

The retrieval process uses cosine similarity to identify the Top-5 most relevant reviews, which are then provided as context to Gemini for answer generation.

**System Workflow**

User Question

      │
      ▼

Sentence Transformer

      │
      ▼

Question Embedding

      │
      ▼

Cosine Similarity

      │
      ▼

Top-5 Relevant Reviews

      │
      ▼

Google Gemini

      │
      ▼

Generated Answer

**Project Structure**

chatgpt-review-rag/

│

├── app.py

├── rag.py

├── processed_reviews.csv

├── GPT_reviews.csv

├── requirements.txt

├── .gitignore

└── README.md

**Installation**

git clone https://github.com/baiqandhini/chatgpt-review-rag.git

cd chatgpt-review-rag

pip install -r requirements.txt

streamlit run app.py

**Deployment**

The application is deployed using

- Streamlit Community Cloud

Google Gemini API key is managed securely using Streamlit Secrets.

Large embedding files are automatically downloaded from Google Drive during initialization to avoid GitHub file size limitations.

**Example Questions**

- Why do users like ChatGPT?

- What improvements do users expect?

- What are the most common issues?

- Is ChatGPT useful for students?

- Overall opinion of users?

**Author**

Baiq Andhini Humaira - 23611058
