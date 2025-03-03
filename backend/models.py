from chatbot import get_chatbot_response
from db import get_db_connection

def process_query(user_query):
    chatbot_response = get_chatbot_response(user_query)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queries (question, answer) VALUES (%s, %s)", (user_query, chatbot_response))

    conn.commit()
    cursor.close()
    conn.close()

    return chatbot_response
