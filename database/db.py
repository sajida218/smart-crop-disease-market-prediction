import sqlite3

conn = sqlite3.connect('database/crop.db')

cursor = conn.cursor()

# Predictions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_name TEXT NOT NULL,
    disease_name TEXT NOT NULL,
    confidence REAL NOT NULL,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database Created Successfully")