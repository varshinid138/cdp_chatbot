# CDP Chatbot

## Overview
The **CDP Chatbot** is a web-based chatbot designed to provide documentation-based answers for Customer Data Platforms (CDPs). It fetches relevant information from various CDP documentation sources, processes queries, and delivers accurate responses using Natural Language Processing (NLP) techniques.

## Features

### 1. **Web Scraping for Documentation**
- Extracts relevant content from:
  - [Zeotap Docs](https://docs.zeotap.com/home/en-us/)
  - [Segment Docs](https://segment.com/docs/?ref=nav)
  - [mParticle Docs](https://docs.mparticle.com/)
  - [Lytics Docs](https://docs.lytics.com/)
- Uses **BeautifulSoup** to parse and clean scraped content.

### 2. **Vector Database for Query Search**
- Stores scraped documentation in a **FAISS (Facebook AI Similarity Search) Vector Database**.
- Uses **Hugging Face embeddings** (`sentence-transformers/all-MiniLM-L6-v2`) to create vectorized representations of documentation.
- Enables efficient similarity-based search for relevant answers.

### 3. **Flask-based API**
- Provides a `/ask` endpoint that:
  - Accepts user queries via a **POST request**.
  - Searches the FAISS vector database for relevant documentation.
  - Returns structured JSON responses.

### 4. **Database for Query Storage**
- Stores user queries and responses in a **MySQL database**.
- Allows tracking of chatbot usage and response accuracy.

### 5. **Frontend Integration (HTML + JavaScript)**
- A simple web interface with:
  - Input field for user questions.
  - Dynamic response display.
  - Error handling for failed API calls.

## Installation

### 1. **Clone the Repository**
```sh
$ git clone <repository-url>
$ cd cdp_chatbot
```

### 2. **Set Up a Virtual Environment (Optional but Recommended)**
```sh
$ python -m venv venv
$ source venv/bin/activate   # On macOS/Linux
$ venv\Scripts\activate     # On Windows
```

### 3. **Install Dependencies**
```sh
$ pip install -r requirements.txt
```

### 4. **Set Up Environment Variables**
Create a `.env` file and add:
```plaintext
OPENAI_API_KEY=your_openai_api_key
MYSQL_USER=root
MYSQL_PASSWORD=tiger
MYSQL_DATABASE=chatbot
```

### 5. **Initialize the Database**
```sh
$ python db.py
```

### 6. **Run the Application**
```sh
$ flask run
```
Access the chatbot UI at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
1. Open the chatbot webpage.
2. Enter a **question** related to CDP documentation.
3. The chatbot fetches relevant data from stored documentation.
4. The response is displayed instantly.

## Project Structure
```
cdp_chatbot/
│── agent.py        # Query processing using FAISS
│── app.py          # Flask API for chatbot interaction
│── chatbot.py      # Core chatbot logic (query processing, scraping)
│── config.py       # MySQL configuration
│── db.py           # Database setup and query storage
│── models.py       # Handles query processing and database integration
│── scraper.py      # Web scraping module for documentation
│── vector_db.py    # FAISS vector storage and retrieval
│── static/
│   ├── styles.css  # Frontend styling
│   ├── app.js      # Frontend logic (AJAX requests, response display)
│── templates/
│   ├── index.html  # Chatbot UI
└── requirements.txt # Python dependencies
```

## Future Enhancements
- Add **authentication** for API security.
- Implement **real-time vector updates**.
- Support additional **CDP documentation sources**.
- Improve **UI/UX** with a chatbot-style interface.

---

**Author:** Varshini Durai Rasu


