import sqlite3

conn = sqlite3.connect('database/crop.db')

cursor = conn.cursor()

cursor.execute("""
INSERT INTO predictions
(image_name,disease_name,confidence)
VALUES
('leaf1.jpg','Tomato Early Blight',95.6)
""")

conn.commit()

conn.close()

print("Data Inserted")