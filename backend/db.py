import pymysql
from config import DB_CONFIG

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
