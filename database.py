import sqlite3

DB_NAME = 'app.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pictures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_type TEXT NOT NULL,
            picture_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_picture(animal_type, picture_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pictures (animal_type, picture_url)
        VALUES (?, ?)
    ''', (animal_type, picture_url))
    conn.commit()
    conn.close()

def get_last_picture(animal_type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT picture_url FROM pictures
        WHERE animal_type = ?
        ORDER BY created_at DESC LIMIT 1
    ''', (animal_type,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

