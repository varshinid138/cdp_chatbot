from scraper import scrape_docs
from vector_db import search_similar_docs

# Function to process user queries
def get_answer(query):
    docs = search_similar_docs(query)  # Use FAISS to retrieve relevant docs
    if not docs:
        return "Sorry, I couldn't find relevant information."

    response = "\n".join([doc.page_content for doc in docs[:3]])  # Return top 3 results
    return response
