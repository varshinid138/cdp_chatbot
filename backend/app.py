from flask import Flask, request, render_template, jsonify
from chatbot import get_chatbot_response
from db import initialize_db
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Initialize DB on startup
initialize_db()

@app.route("/")
def home():
    return render_template("index.html")

import logging

logging.basicConfig(level=logging.DEBUG)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("query")
    logging.debug(f"Received query: {question}")
    
    if not question:
        return jsonify({"error": "No query provided"}), 400

    try:
        answer = get_chatbot_response(question)
        logging.debug(f"Chatbot response: {answer}")

        if not answer.strip():
            return jsonify({"error": "Chatbot returned an empty response"}), 500

        return jsonify({"question": question, "answer": answer})
    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
