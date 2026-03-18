<<<<<<< HEAD
# AI Knowledge Assistant — Emanager Endee

## Project Overview
AI Knowledge Assistant is a web-based AI system that answers questions using a curated knowledge base (`data/knowledge.txt`). The system converts documents into vector embeddings and uses semantic search to return the most relevant answer to a user's query.  

This project demonstrates how to build a simple AI-powered semantic search system using Endee vector database principles and Sentence Transformers.

---

## Architecture


User Query
↓
Semantic Search (documents.txt)
↓
Best Matching Answer
↓
Displayed on Web Interface / Console


---

## Features

- Semantic search using vector embeddings (Sentence Transformers).  
- Knowledge base stored in `data/documents.txt`.  
- Converts text documents → embeddings → vectors.  
- Returns the best matching document for a user query.  
- Clean structure suitable for GitHub and deployment.

---

## Setup Instructions

1. Clone the repository:

```bash
git clone YOUR_REPO_LINK
cd AI-KNOWLEDGE_ASSISTANT_ENDEE

Create a virtual environment (recommended):

# Using conda
conda create -n endee_project python=3.14
conda activate endee_project

# Or using venv
python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Store vector embeddings:

python src/store_vectors.py

Run the application:

python -m app.py
# Or using Streamlit
python -m streamlit run streamlit_app.py

Start asking questions and get answers from your knowledge base.

Example Usage

Question: What is artificial intelligence?
Answer: Artificial Intelligence is the simulation of human intelligence by machines.

Question: What is machine learning?
Answer: Machine learning is a subset of AI that allows computers to learn from data.

Question: What is deep learning?
Answer: Deep learning is a technique that uses neural networks.

Project Structure
AI-KNOWLEDGE_ASSISTANT_ENDEE/
│
├── data/
│   └── documents.txt       # Knowledge base documents
├── src/
│   ├── embeddings.py       # Embedding generator
│   ├── store_vectors.py    # Convert documents → vectors
│   └── search.py           # Semantic search logic
├── app.py                  # Main application (console or Streamlit)
├── requirements.txt        # Dependencies
└── README.md               # Project description
Technologies Used

Python 3.14

Numpy

Pandas

Sentence-Transformers

Streamlit (optional for web interface)

Future Improvements

Display top 3 most relevant answers instead of just one.

Enhance knowledge base with more documents.

Deploy as a web app for easy access.

Add colored chat bubbles and better UI for Streamlit.

Author

Tejashwini N M
Email: tejashwininmteju@gmail.com

GitHub: https://github.com/TejashwiniNM


