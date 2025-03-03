import os
import requests
from bs4 import BeautifulSoup
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from vector_db import search_similar_docs

# Load environment variables
load_dotenv()

# Use Hugging Face embeddings instead of OpenAI
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# List of documentation sources
DOC_SOURCES = [
    "https://docs.zeotap.com/home/en-us/",
    "https://segment.com/docs/?ref=nav",
    "https://docs.mparticle.com/",
    "https://docs.lytics.com/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com"
}

def fetch_page_content(url):
    """ Fetch webpage content from a given URL. """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        return f"Error fetching {url}: {str(e)}"

def get_chatbot_response(query):
    """ Search FAISS vector DB for relevant documentation and return response. """
    docs = search_similar_docs(query)  # Use FAISS DB to fetch relevant docs

    if not docs:
        return "Sorry, I couldn't find relevant documentation at the moment."

    response = "\n".join([doc.page_content for doc in docs[:3]])  # Return top 3 docs
    return response
