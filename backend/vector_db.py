import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from scraper import scrape_docs

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Use Hugging Face embeddings to avoid OpenAI rate limits
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def store_embeddings():
    """Scrape & store CDP documentation embeddings in FAISS vector DB in small batches."""
    docs = {cdp: scrape_docs(cdp) for cdp in CDP_DOCS.keys()}
    texts = [f"{cdp}: {text}" for cdp, text in docs.items()]
    
    vector_db = None
    batch_size = 2  # Reduce the number of documents processed at a time

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        if vector_db is None:
            vector_db = FAISS.from_texts(batch, embeddings)
        else:
            vector_db.add_texts(batch)

    vector_db.save_local("faiss_index")

def search_similar_docs(query):
    """Retrieve relevant documentation based on query."""
    vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = vector_db.similarity_search(query)
    return docs
